from BD import BD

bd = BD('localhost',3307,'administracion','root','intendo64R')

bd.selectCondition("*","usuario","nombre = pepe")

bd.selectSimple("*","agente")