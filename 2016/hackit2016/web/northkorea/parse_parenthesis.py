text = "(])[(]}]}][}}()}}]]]({)]{{})}}]{])([[}]])}{}(({()}}]]]({{}((()[()})){)({)}]){([{[[{[}))}()(({[{(([{}{]]})])[{)[)][{][))]}][]{][}}}(}((]{{[){{[)(}}]{{])}(][){}][)())[}{{}([[}[{]}{[)[}})[[{}{[]]({(]{([([](})([}[](}}((}(]][({}}{(]]){[(})})}{[}}[[){}[){{][}){)[}{)[[(}({}{{))]){)[})[)}](({(){]([[)({)(}]}[}))(}}[}){[){][}][){[}{}{]]))]}{({][)}((([]){]({{})}}]}}[))){[][}(({){{][})([])]]}]])}])[}({({)](}{]}{}}][[{[[}(])(])[}}](}{)](}]]}{{)}}))))}){]{[{([])[(}(((((}[[}[})()}[]]{}[[)})(()])}{[{())[[)(]}[{](}]()[])[([{[{{[}}}}]}[{)[)}}{{[)([[]([}}[][]]}}[[{](}}{([{[]){({}]}}{[}()){]{}){[}{(({[{([}[}({(]}])}({)]])])}]([}{]]{({(}{[))(({[)(]{))[[]{[)}(][{]])}]]([)[)]][]]]}(}}{{{{}}][({[{}(}[}{{(}))}{((}(([{})}]{[[({()())))))(()}[{){[]{({]{}[)[(}}[)[[]{){])[)[((]}}){]{][{[){){])]}}{([{]}{[{([(([[)}]}}()[{][}][]{})(({[{{][})([(((}{)){}])))}]{)([{{}{{}(}}))(({]])}[)](][(}[{{}([(])({[()[[}{({(}{]{}[{))]({}{()(([{}]((}][}(}]){]}([(})[)]]][}{][{(((}}{}{]}])](}({}([{])}}{}[{}{]]]})([][)[(](}}[][()(}]}[[}{}[[(}({[[]())][])}(]})}})))}}[[{}[[[({()(]}()}(})[[}[]}}))}}({]({{)}][}[]]()]}{{]}))}([[(]}{]()}[)(}{(}]([[])[{]}){()}})}][)}}](()(]}){])(]{(([({[](}{([[(){{{)][)[)]{[{]}]]}{){{{((}}([]({{][)(}{)()([({]{([{}({))}]}[[][][{([[{)))())(}{(([]}{{({[({}{)[{]]]]])({{{}][}(}]}{}[}}}[{]{[)})})){){}{[)}){}}[]((}()[()[)}{{{){(][)][()}]]()[[({()(({[((())}](}){})()[])[}([])])}[{)[](]}(]()}]]}[([{{[)([[}[[}[}]]{]{({}(]{))}}({]}[[]{}[}[}{){[}}}]{[(}])})]{{(](]]})[}(()]][}{}}](]{}}(}}){]({(])[[)))}]){}(}{]](]]({}])(()[]{))(([[}){]}((])[{)(}]]([)]{)){}[{))}([({}[{()}]}))((][({)]{}]]([{({](}[{){{[{{)]([{)[{}){}{}}){[}]}}](}(]}])(}))())))])]]}}{)(}}{[[}()({[{[[){{]}[)[{}[}){(][[)]))][][])}[}(}[([](]}({{(]}]}{)}[}})][}]{{)}([{[{]}]{{]})}{]]([)[)()][){][]))){][{{(([)](]})]]){{])]]{()]){})}})(()))){))})(((([}{)][}[)}[({)])}){}]([[][{])}))[)[}]}[}[}})][((]{{}}{}]])[[)()([(}][}][{])][([([)}{)}})[([(([[))[[[}([)[{)](}){{[(])((([{]]}[(})[()}}()}(]{)(]}[))]})[)][)}}(){)])([)]{[{{){)]])()}(()(({}[}[{)[[[(}[){]{}{)]{}[)}[]}((][){}][{{[}}}]{{}[{([{{}[)[]()(()[){{"

n = [0,0,0,0,0,0]
answer =""
#    (,),[,],{,}
for i in text:
  if i == "(":
    n[0] += 1
    answer += "("
  elif i == ")":
    if(n[0] > 0):
      n[0] -= 1
      answer += ")"
    else:
      answer += "()"
  elif i == "[":
    n[2] += 1
    answer += "["
  elif i == "]":
    if(n[2] > 0):
      n[2] -= 1
      answer += "]"
    else:
      answer+="[]"
  elif i == "{":
    n[4] += 1
    answer += "{"
  elif i == "}":
    if n[4]>0:
      n[4]-=1
      answer += "}"
    else:
      answer+="{}"

while n[0] > 0:
  answer += ")"
  n[0] -= 1
while  n[2] > 0:
  answer += "]"
  n[2] -= 1
while  n[4] > 0:
  answer += "}"
  n[4] -= 1


print answer
