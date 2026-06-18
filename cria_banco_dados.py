import pandas as pd

# Extração estruturada baseada no seu PDF
dados_iniciais = [
    # ------------------------------
    # Embutidos e Carnes Processadas
    # ------------------------------
    {
        "Categoria": "Embutidos e Carnes Processadas",
        "Alimento": "Salsicha Sadia",
        "Descricao": "Carne mecanicamente separada, gordura e conservantes, muito usada em cachorros-quentes.",
        "Porcao": "Nutriente Porção 100g",
        "Valor_Energético": "212 kcal",
        "Carboidratos": "2 g",
        "Açúcares_Totais": "0 g",
        "Açúcares_Adicionados": "0 g",
        "Proteínas": "15 g",
        "Gorduras_Totais": "16 g",
        "Gorduras Saturadas": "5,9 g",
        "Gorduras_Trans": "0 g",
        "Fibra Alimentar": "0 g",
        "Sódio": "976 mg",
        "Nivel_Risco_Pct": 00, # Valor sugerido para o gráfico
        "Alerta_Riscos": "Comer até duas salsichas por semana é seguro. O excesso causa câncer no intestino, pressão alta, infarto e sobrecarga nos rins.",
        "Caminho_Imagem": "imagens/salsicha.png"
    },

    
    {
        "Categoria": "Embutidos e Carnes Processadas",
        "Alimento": "Nuggets Sadia",
        "Descricao": "Mistura de carne de frango processada, moldada e coberta por uma camada crocante para fritar.",
        "Porcao": "Nutriente porção de 130g (6 unidades) contém aproximadamente:",
        "Valor_Energético": "261 kcal", 
        "Carboidratos": "21 g", 
        "Proteínas": "18 g", 
        "Gorduras Totais": "12 g", 
        "Gorduras Saturadas": "3,1 g", 
        "Gorduras Trans": "0 g", 
        "Fibra Alimentar": "1,6 g", 
        "Sódio": "590 mg", 
        "Nivel_Risco_Pct": 00, # Valor sugerido para o gráfico
        "Alerta_Riscos": "Comer até quatro nuggets por semana (cerca de 50g) é seguro, mas passar disso e consumir diariamente é maléfico porque causa pressão alta, ganho de peso, gordura no fígado e problemas no coração.",
        "Caminho_Imagem": "imagens/nuggets.png"
    },


    {
        "Categoria": "Embutidos e Carnes Processadas",
        "Alimento": "Mortadela Sadia",
        "Descricao": "Embutido de carne moída com cubos de gordura, amido e temperos industriais.",
        "Porcao": "Nutriente Porção (100g)",
        "Valor_Energético": "298 kcal", 
        "Carboidratos": "4,8 g", 
        "Proteínas": "14 g", 
        "Gorduras Totais": "25 g", 
        "Gorduras Saturadas": "7,2 g", 
        "Gorduras Trans": "0 g", 
        "Fibra Alimentar": "0 g", 
        "Sódio": "1,165 mg", 
        "Nivel_Risco_Pct": 00, # Valor sugerido para o gráfico
        "Alerta_Riscos": "Comer até duas fatias de mortadela por semana (cerca de 30g) é seguro, mas passar disso e consumir diariamente é maléfico porque causa câncer no intestino, pressão alta, retenção de líquido e infarto.",
        "Caminho_Imagem": "imagens/mortadela.png"
    },


    {
        "Categoria": "Embutidos e Carnes Processadas",
        "Alimento": "Hamburguer congelado Sadia",
        "Descricao": "Discos de carne altamente processada e temperada, prontos para a chapa.",
        "Porcao": "Nutriente Porção 80g",
        "Valor_Energético": "225 kcal", 
        "Carboidratos": "3 g", 
        "Proteínas": "15 g", 
        "Gorduras Totais": "17,5 g", 
        "Gorduras Saturadas": "5,1 g", 
        "Gorduras Trans": "0 g", 
        "Fibra Alimentar": "1,3 g", 
        "Sódio": "465 mg", 
        "Nivel_Risco_Pct": 00, # Valor sugerido para o gráfico
        "Alerta_Riscos": "A quantidade máxima segura para consumir o hambúrguer congelado tradicional da Sadia é de no máximo 1 unidade por dia (80g), limitando esse consumo a 1 ou 2 vezes por semana.",
        "Caminho_Imagem": "imagens/hamburguer_congelado.png"
    },


    {
        "Categoria": "Embutidos e Carnes Processadas",
        "Alimento": "Calabresa industrializada Sadia",
        "Descricao": "Linguiça defumada artificialmente, rica em sódio e conservantes (fixadores de cor).",
        "Porcao": "Nutriente Porção 100g",
        "Valor_Energético": "332 kcal", 
        "Carboidratos": "2 g",
        "Açúcares_Totais": "1,7 g",
        "Açúcares_Adicionados": "1 g", 
        "Proteínas": "18 g", 
        "Gorduras Totais": "28 g", 
        "Gorduras Saturadas": "11 g", 
        "Gorduras Trans": "0 g", 
        "Fibra Alimentar": "0 g", 
        "Sódio": "1,360 mg", 
        "Nivel_Risco_Pct": 00, # Valor sugerido para o gráfico
        "Alerta_Riscos": "A quantidade máxima segura para consumir o hambúrguer congelado tradicional da Sadia é de no máximo 1 unidade por dia (80g), limitando esse consumo a 1 ou 2 vezes por semana.",
        "Caminho_Imagem": "imagens/calabresa.png"
    },



    # ------------------------------------
    # Pratos Prontos e Massas Instantâneas
    # ------------------------------------

    {
        "Categoria": "Pratos Prontos e Massas Instantâneas",
        "Alimento": "Macarrão industrializado (Miojo)",
        "Descricao": "Massa frita e desidratada que cozinha rápido, acompanhada de sachê com tempero concentrado",
        "Porcao": "Nutriente Porção média (por pacote de 85 g)",
        "Valor_Energético": "374 a 435 kcal", 
        "Carboidratos": "49 a 58 g",
        "Gorduras Totais": "13 a 17 g (geralmente por ser pré-frito)",
        "Gorduras Saturadas": "5 a 7 g",
        "Proteínas": "8 a 10 g", 
        "Sódio": "1,300 a 2.000 mg (dependendo do sabor) - O que ultrapassa ou chega muito proximo ao limite diário recomendado pela OMS", 
        "Nivel_Risco_Pct": 00, # Valor sugerido para o gráfico
        "Alerta_Riscos": "O ideal recomendado por cardiologistas e nutricionistas é evitar o consumo ou limitá-lo a 1 vez a cada 15 dias, pois ele é um dos ultraprocessados mais agressivos para o sistema cardiovascular devido à fritura da massa e ao tempero em pó.",
        "Caminho_Imagem": "imagens/miojo.png"
    },

    {
        "Categoria": "Pratos Prontos e Massas Instantâneas",
        "Alimento": "Cup noodles",
        "Descricao": "Versão de macarrão instantâneo em copo com pequenos pedaços de vegetais e carnes desidratadas.",
        "Porcao": "Nutriente Porção de 69g (1 copo)",
        "Valor_Energético": "318 kcal", 
        "Carboidratos": "43 g", 
        "Proteínas": "7,2 g", 
        "Gorduras Totais": "13 g", 
        "Gorduras Saturadas": "6,1 g", 
        "Gorduras Trans": "0 g", 
        "Fibra Alimentar": "2,0 g", 
        "Sódio": "1188 mg", 
        "Nivel_Risco_Pct": 00, # Valor sugerido para o gráfico
        "Alerta_Riscos": "A quantidade máxima segura para consumir o Cup Noodles é de no máximo 1 copo por semana, devendo ser evitado ou consumido apenas 1 vez a cada 15 dias.",
        "Caminho_Imagem": "imagens/cup_noodles.png"
    },

    {
        "Categoria": "Pratos Prontos e Massas Instantâneas",
        "Alimento": "Pizza congelada Sadia",
        "Descricao": "Massa pré-assada com molho e queijo processado, pronta para ir direto ao forno.",
        "Porcao": "Nutriente Porção (100g)",
        "Valor_Energético": "247 kcal", 
        "Carboidratos": "25 g",
        "Açúcares_Totais": "2,7 g",
        "Açúcares_Adicionados": "0,7 g", 
        "Proteínas": "12 g", 
        "Gorduras Totais": "11 g", 
        "Gorduras Saturadas": "4,4 g", 
        "Gorduras Trans": "0 g", 
        "Fibra Alimentar": "2,4 g", 
        "Sódio": "451 mg", 
        "Nivel_Risco_Pct": 00, # Valor sugerido para o gráfico
        "Alerta_Riscos": "A porção padrão indicada pela própria marca no rótulo é de 77g (o equivalente a 1/6 da pizza). Comer mais do que 3 fatias em uma única refeição ultrapassa os limites diários saudáveis de gordura e sódio estabelecidos por cardiologistas.",
        "Caminho_Imagem": "imagens/pizza.png"
    },

    {
        "Categoria": "Pratos Prontos e Massas Instantâneas",
        "Alimento": "Lasanha congelada de micro-ondas Sadia",
        "Descricao": "Prato pronto com várias camadas de massa, molho industrial e carne ou queijo, focado na praticidade rápida.",
        "Porcao": "Nutriente Porção (100g)",
        "Valor_Energético": "125 kcal", 
        "Carboidratos": "10 g",
        "Açúcares_Totais": "1,9 g",
        "Açúcares_Adicionados": "0,4 g", 
        "Proteínas": "8,6 g", 
        "Gorduras Totais": "5,6 g", 
        "Gorduras Saturadas": "2,9 g", 
        "Gorduras Trans": "0 g", 
        "Fibra Alimentar": "1,7 g", 
        "Sódio": "310 mg", 
        "Nivel_Risco_Pct": 00, # Valor sugerido para o gráfico
        "Alerta_Riscos": "A quantidade segura recomendada para consumo é de no máximo 1 porção de 100g a 150g por refeição, o que equivale a menos da metade da embalagem pequena (350g) ou a um quarto da embalagem média (600g).",
        "Caminho_Imagem": "imagens/lasanha.png"
    },


    # ------------------------------
    # Snacks e Salgadinhos de Pacote
    # ------------------------------

    {
        "Categoria": "Snacks e Salgadinhos de Pacote",
        "Alimento": "Salgadinho de milho (Doritos)",
        "Descricao": "Snacks extrusados (moldados sob alta pressão e temperatura) com pós saborizantes artificiais intensos.",
        "Porcao": "Informação Nutricional",
        "Valor_Energético": "120 kcal", 
        "Carboidratos": "16 g",
        "Açúcares_Totais": "0,5 g",
        "Açúcares_Adicionados": "0,2 g", 
        "Proteínas": "1,6 g", 
        "Gorduras Totais": "6,0 g", 
        "Gorduras Saturadas": "0,9 g", 
        "Gorduras Trans": "0,1 g", 
        "Fibra Alimentar": "0,5 g", 
        "Sódio": "144 mg", 
        "Nivel_Risco_Pct": 00, # Valor sugerido para o gráfico
        "Alerta_Riscos": "A quantidade segura para consumir Doritos é de no máximo 25g a 30g de forma bem ocasional. Se você ultrapassar esse limite e consumir em excesso, o produto pode causar riscos sérios à saúde, como pressão alta, obesidade, inflamações digestivas e problemas cardíacos devido ao excesso de sódio, corantes e gorduras.",
        "Caminho_Imagem": "imagens/doritos.png"
    },

    {
        "Categoria": "Snacks e Salgadinhos de Pacote",
        "Alimento": "Batata Chips de tupo (Pringles)",
        "Descricao": "Batatas formadas a partir de uma massa de flocos de batata e amidos desidratados.",
        "Porcao": "Por porção 100g",
        "Valor_Energético": "528 kcal",
        "Lípidos": "31 g dos quais saturados 3 g",
        "Hidratos_de_Carbono": "54 g dos quais açúcares 0,9 g", 
        "Fibra": "4.1 g",
        "Proteínas": "6,2 g",
        "Sal": " 1,0 g",
        "Nivel_Risco_Pct": 00, # Valor sugerido para o gráfico
        "Alerta_Riscos": "A quantidade segura para consumir Pringles é de no máximo 25g (cerca de 13 batatas) de forma ocasional. Se você ultrapassar esse limite e consumir em excesso, o produto pode causar riscos à saúde, como pressão alta, ganho de peso, retenção de líquido e problemas cardíacos pelo excesso de sódio e gorduras saturadas.",
        "Caminho_Imagem": "imagens/pringles.png"
    },

    {
        "Categoria": "Snacks e Salgadinhos de Pacote",
        "Alimento": "Biscoito de polvilho industrialisado (Bebela)",
        "Descricao": "Versão de pacote que leva gordura vegetal hidrogenada para garantir a crocância por meses.",
        "Porcao": "Por porção 100g",
        "Valor_Energético": "430 kcal", 
        "Carboidratos": "68 g",
        "Açúcares_Totais": "0 g",
        "Açúcares_Adicionados": "0 g", 
        "Proteínas": "0 g", 
        "Gorduras_Totais": "17 g", 
        "Gorduras_Saturadas": "12 g", 
        "Gorduras_Trans": "0 g", 
        "Fibra_Alimentar": "0 g", 
        "Sódio": "886 mg", 
        "Nivel_Risco_Pct": 00, # Valor sugerido para o gráfico
        "Alerta_Riscos": "A quantidade segura para consumir biscoito de polvilho industrializado é de no máximo 25g a 30g de forma ocasional. Se você ultrapassar esse limite e consumir em excesso, o produto pode causar riscos à saúde, como pressão alta, retenção de líquido e ganho de peso, devido ao altíssimo teor de sódio e gorduras que o processo industrial adiciona.",
        "Caminho_Imagem": "imagens/bebela.png"
    },

 
    # --------------------------------
    # Bebidas e Doces Ultraprocessados
    # --------------------------------
    {
        "Categoria": "Bebidas e Doces Ultraprocessados",
        "Alimento": "Coca-Cola Lata 350 ml",
        "Descricao": "Mistura de água gaseificada, xarope de milho (açúcar), corantes e acidulantes.",
        "Porcao": "Informação Nutricional Quantidade por 350 ml",
        "Valor_Energético": "149 154 kcal", 
        "Carboidratos": "37 a 39 g",
        "Açúcares_Totais": "37 a 39 g",
        "Sodio": "10 a 18 mg", 
        "Proteínas": "0 g", 
        "Gorduras": "0 g",  
        "Nivel_Risco_Pct": 00, # Valor sugerido para o gráfico
        "Alerta_Riscos": "A quantidade segura para consumir Coca-Cola de 350ml é de no máximo uma lata ocasional, idealmente evitando o consumo semanal. Se você ultrapassar esse limite e consumir em excesso, o produto pode causar riscos à saúde, como diabetes tipo 2, obesidade, cáries, gordura no fígado e pressão alta devido ao altíssimo teor de açúcar e compostos químicos. ",
        "Caminho_Imagem": "imagens/coca_cola.png"
    },

    {
        "Categoria": "Bebidas e Doces Ultraprocessados",
        "Alimento": "Achocolatado de caixinha (Todinho)",
        "Descricao": "Bebida láctea pronta com soro de leite, muito açúcar, espessantes e estabilizantes",
        "Porcao": "Informação Nutricional Quantidade por 200ml (1 unidade)",
        "Valor_Energético": "185 kcal", 
        "Carboidratos": "32 g",
        "Açúcares": "29 g", 
        "Proteínas": "3,9 g", 
        "Gorduras_Trans": "0 g",
        "Gorduras_Totais": "4,7 g", 
        "Gorduras_Saturadas": "2,1 g", 
        "Fibra_Alimentar": "0 g", 
        "Sódio": "130 mg",
        "Cálcio": "107 mg",
        "Ferro": "1,8 mg",
        "Vitamina A": "135 mcg",
        "Vitamina C": "9,0 mg",
        "Ácido Fólico": "35 mg", 
        "Nivel_Risco_Pct": 00, # Valor sugerido para o gráfico
        "Alerta_Riscos": "A quantidade segura para consumir achocolatado de caixinha (como Toddynho) é de no máximo uma unidade (200ml) ocasional, evitando o consumo diário. Se você ultrapassar esse limite e consumir em excesso, o produto pode causar riscos à saúde, como obesidade infantil, diabetes, cáries e gordura no fígado, devido à enorme quantidade de açúcar refinado e aditivos. ",
        "Caminho_Imagem": "imagens/todinho.png"
    },

    {
        "Categoria": "Bebidas e Doces Ultraprocessados",
        "Alimento": "Biscoito recheado Piraquê (Sabor chocolate)",
        "Descricao": "Bolachas doces com recheio feito basicamente de gordura vegetal, açúcar e aromas artificiais.",
        "Porcao": "Quantidade por porção (1 unidade)",
        "Valor_Energético": "143 kcal", 
        "Carboidratos": "20 g",
        "Açúcares_Totais": "11 g",
        "Açúcares_Adicionados": "11 g", 
        "Proteínas": "1,9 g", 
        "Gorduras Totais": "6,1 g", 
        "Gorduras Saturadas": "2,6 g", 
        "Gorduras Trans": "0,1 g", 
        "Fibra Alimentar": "0,7 g", 
        "Sódio": "61 mg", 
        "Nivel_Risco_Pct": 00, # Valor sugerido para o gráfico
        "Alerta_Riscos": "A quantidade segura para consumir biscoito recheado Piraquê de chocolate é de no máximo 2 a 3 unidades(cerca de 30g) de forma bem ocasional. Se você ultrapassar esse limite e consumir em excesso, o produto pode causar riscos à saúde, como ganho de peso, diabetes, colesterol alto e gordura no fígado, devido ao altíssimo teor de açúcar refinado e gordura vegetal.",
        "Caminho_Imagem": "imagens/piraque.png"
    }
]

# Cria o DataFrame e exporta para Excel
df = pd.DataFrame(dados_iniciais)
df.to_excel("banco_alimentos.xlsx", index=False)
print("Arquivo Excel 'banco_alimentos.xlsx' criado com sucesso!")