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
PartPZeroVoiceOne =  \relative dis' {
    \clef "treble" \numericTimeSignature\time 4/4 \key c \major | % 1
    dis4 cis4 eis4 ces'4 eis,4 des'4 fis,4 fes4 es4 ces4 eis4 des'4 fis,4
    fes4 es4 ces4 | % 2
    eis4 des4 es4 ces4 fis4 cis4 eis4 dis4 fis4 fes4 fis4 cis4 es4 ces4
    eis4 eis4 | % 3
    eis4 des'4 eis,4 cis'4 eis,4 dis4 es4 ces4 fis4 fis4 eis4 des'4 fis,4
    cis4 eis4 ces'4 | % 4
    es,4 ces4 fis4 fes4 eis4 fis'4 eis,4 dis'4 eis,4 dis4 es4 ces4 fis4
    fes4 eis4 des4 | % 5
    eis4 dis'4 fis,4 ces4 eis4 cis'4 eis,4 dis4 es4 ces4 fis4 cis4 eis4
    dis4 fis4 ces'4 | % 6
    fis,4 cis4 es4 des4 ces4 es'4 ces,4 es'4 }


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

