# ^ coresponde a iniciar de uma linha
# $ corresponde ao fim da linha
# . corresponde aqualquer caracter
# \s corresponde a espaço em branco
# \S corresponde a qualquer não espaço branco caracter
# * repete um caracter zero ou mais vezes
# *? repete um caracter zero ou mais vezes (nem-tanto)
# + repete um caracter uma ou mais vezes
# +? repete um caracter uma ou mais vezes (nem-tanto)
# [aeiou] corresponde a unico caracter na lista definida
# [^XYZ] corresponde um unico caracter não no conjunto listada 
# [a-z0-9] O conjunto de caracteres pode incluir um alcance # ( indica onde a extração do string é para iniciar
# ) inidica onde a extração do string vai terminar

#corresponde a 
# inicio da linha  - qualquer espaço em caracter nao branco- uma ou mais vezes ^X-\S+:
#x-sieve: *cmu sieve 2.3*
#x-dspam-result: *innocent* 
# *x-plane is behind schedule: two weeks*


#  corresponde a
# iniciao da linha - qualquer caracter - vezes vezes ^X.*:
#x-sieve: *cmu sieve 2.3*
#x-dspam-result: *innocent* 
#x-dspam-confidence: *0.8475*
#x-content-type-message-body: *text/plain*

# Correspondendo e extraido dado
# re-search() return true/false dependo em se o string corrsponde a regular expressao
# if nos na verdade queremso corresponder string por ser extraido, usamos re.findall()
#[0-9]+ um ou mais digitos