#%%
import spacy
from sentence_transformers import SentenceTransformer, util
# 1️⃣ Carregar o spaCy para pré-processamento
nlp = spacy.load("pt_core_news_lg")


# %%
# 2️⃣ Carregar o modelo semântico
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

# 3️⃣ Dicionário FAQ
faq = {
    "minha máquina de lavar não está ligando": "Verifique se o cabo de energia está bem conectado e se há energia na tomada. Se o problema persistir, entre em contato com a assistência técnica.",
    "a máquina de lavar está fazendo barulho": "Certifique-se de que não há moedas, botões ou objetos soltos no tambor. Barulhos fortes também podem indicar desequilíbrio na carga.",
    "como limpar o filtro da máquina de lavar": "Desligue a máquina da tomada, abra a tampa inferior e retire o filtro girando-o no sentido anti-horário. Lave com água corrente e recoloque.",
    "a roupa sai muito molhada da máquina": "Verifique se o ciclo de centrifugação está selecionado corretamente. Cargas muito grandes ou mal distribuídas podem afetar o desempenho.",
    "como faço para usar o modo econômico da máquina": "Selecione o ciclo ‘Econômico’ ou ‘Rápido’ no painel e use a quantidade de sabão indicada no manual. Isso economiza água e energia.",
    "a máquina está com mau cheiro": "Recomenda-se fazer uma lavagem com o tambor vazio, utilizando vinagre branco ou produtos específicos para limpeza de máquinas.",
    "meu fogão não está acendendo": "Verifique se o gás está aberto e se o acendimento automático está funcionando. Caso use fósforo, veja se o queimador não está entupido.",
    "a chama do fogão está amarela": "Isso pode indicar sujeira ou pouca entrada de oxigênio. Retire o queimador e limpe-o com cuidado.",
    "como limpar o forno do fogão": "Use um pano úmido com detergente neutro. Evite produtos abrasivos. Para sujeiras pesadas, use vinagre morno e bicarbonato.",
    "meu forno não aquece direito": "Verifique se o seletor de temperatura está funcionando e se o acendimento está completo. Caso o problema continue, pode ser falha no termostato.",
    "como saber o tamanho do botijão ideal": "Verifique o manual do seu modelo. A maioria dos fogões domésticos utiliza botijões de 13 kg com válvula padrão.",
    "quanto tempo dura o acendimento automático": "Depende do modelo, mas em média o acendimento deve ocorrer em até 3 segundos após pressionar o botão."
}

# 4️⃣ Função pra limpar e normalizar o texto
def preprocessar(texto):
    doc = nlp(texto.lower())
    tokens_validos = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens_validos)

# 5️⃣ Pré-processar todas as perguntas do FAQ
faq_list = list(faq.keys())
faq_processadas = [preprocessar(pergunta) for pergunta in faq_list]
# %%
# 6️⃣ Gerar embeddings (só precisa fazer uma vez)
faq_embeddings = model.encode(faq_processadas, convert_to_tensor=True)

# 7️⃣ Entrada do usuário
usuario_input = input("Digite sua dúvida: ")
usuario_limpo = preprocessar(usuario_input)
usuario_embedding = model.encode(usuario_limpo, convert_to_tensor=True)


# %%
# 8️⃣ Calcular similaridade
similaridades = util.cos_sim(usuario_embedding, faq_embeddings)[0]
indice = similaridades.argmax().item()
melhor_pergunta = faq_list[indice]
melhor_resposta = faq[melhor_pergunta]
pontuacao = similaridades[indice].item()

# 9️⃣ Exibir resultado
print("\nMelhor correspondência:")
print(f"Pergunta: {melhor_pergunta}")
print(f"Similaridade: {pontuacao*100:.2f}%")
print(f"Resposta: {melhor_resposta}")

#  🔟 Opcional: verificação de confiança
if pontuacao < 0.6:
    print("\n⚠️ Não encontrei uma resposta exata para sua pergunta.")