\version "2.24.4"
% automatically converted by musicxml2ly from test_data/sample_music.musicxml
\pointAndClickOff

\header {
    }

\layout {
    \context { \Score
        autoBeaming = ##f
        }
    }
PartPZeroVoiceOne =  \relative fis' {
    \clef "treble" \numericTimeSignature\time 4/4 \key c \major | % 1
    fis4 fes'4 ces,4 es'4 es,4 ces4 es4 ces4 es4 ces4 es4 ces4 es4 es4
    eis4 eis'4 | % 2
    eis,4 des4 eis4 dis'4 eis,4 dis4 es4 es4 fes4 es'4 es,4 ces4 es4 es4
    dis4 cis4 | % 3
    fis4 des'4 fis,4 es4 eis4 des'4 eis,4 fis'4 eis,4 eis'4 es,4 ces4
    cis4 cis'4 eis,4 des4 | % 4
    eis4 eis'4 eis,4 eis'4 eis,4 des'4 fis,4 fes4 fis4 cis4 eis4 dis4
    fis4 es4 es4 es4 | % 5
    es4 cis'4 ces,4 es'4 es,4 ces4 es4 ces4 es4 ces4 es4 ces4 es4 es4
    eis4 des4 | % 6
    eis4 fis4 eis4 dis4 es4 es4 fes4 es'4 es,4 ces4 fes4 es4 fes4 cis4
    es4 cis'4 | % 7
    ces,4 es'4 es,4 ces4 es4 ces4 es4 ces4 es4 ces4 es4 es4 fis4 cis4
    eis4 cis'4 | % 8
    eis,4 cis4 fis4 es4 es4 es4 fes4 es'4 es,4 ces4 es4 es4 cis4 cis4
    fis4 es4 | % 9
    eis4 des'4 eis,4 eis'4 eis,4 fes'4 fis,4 fes4 es4 ces4 eis4 des4 eis4
    eis'4 eis,4 cis4 | \barNumberCheck #10
    es4 ces4 eis4 fes'4 eis,4 eis'4 eis,4 fis'4 fis,4 fis4 fis4 fes4 es4
    ces4 fis4 cis4 | % 11
    eis4 ces'4 eis,4 des'4 eis,4 eis'4 eis,4 fis4 fis4 fes4 es4 es4 ces4
    es'4 fis,4 dis'4 }


% The score definition
\score {
    <<
        
        \new Staff
        <<
            \set Staff.instrumentName = "Sample Text"
            
            \context Staff << 
                \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                \context Voice = "PartPZeroVoiceOne" {  \PartPZeroVoiceOne }
                >>
            >>
        
        >>
    \layout {}
    \midi { }
}

