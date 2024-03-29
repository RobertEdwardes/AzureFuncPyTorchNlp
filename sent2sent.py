import torch
def sent2sent (sentence1, sentence2):
    predic_out= {0:'contradiction', 1:'neutral', 2:'entailment'}
    roberta = torch.hub.load('pytorch/fairseq', 'roberta.large.mnli')
    roberta.eval()
    with torch.no_grad():
        tokens = roberta.encode(sentence1, sentence2)
        prediction = roberta.predict('mnli', tokens).argmax().item()
        return predic_out[prediction]