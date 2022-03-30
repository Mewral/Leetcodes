from torch import nn
import torch

class NNLM:
    def __init__(self):
        self.c = nn.Embedding(n_class, m)
        self.H = nn.Linear(n_step*m, n_hidden, bias=False)






if __name__ == '__main__':
    n_step = 2
    n_hidden = 2
    m = 2

    nn.Parameter
    torch.eye()
    a = nn.Embedding(11, 3)
    t = torch.LongTensor([[1, 0], [0, 1]])
    s = torch.FloatTensor([[1, 0], [0, 1]])
    b = nn.Linear(2, 3)
    print(a(t))
    print(b(s))
    # embeddding(10,3)
    # tensor([[[-0.5074, 1.0402, -0.7596],
    #          [-0.9460, -0.9129, -2.3212],
    #          [-0.4100, -0.0365, -0.4120],
    #          [1.0130, -0.3217, -1.7421]],
    #
    #         [[0.6077, 0.2186, 2.5427],
    #          [2.0317, 2.8008, -1.2431],
    #          [-0.4673, -1.2594, -0.8288],
    #          [-0.3661, 0.1637, -0.4323]]], grad_fn= < EmbeddingBackward0 >)

    # embedding (11,3)
    # tensor([[[0.4778, -1.3051, -0.1616],
    #          [0.3008, -0.1178, -2.5099],
    #          [0.6611, 0.1144, -0.9280],
    #          [-0.6110, -0.6532, -2.1349]],
    #
    #         [[-0.7906, 1.1016, 1.0408],
    #          [-0.6580, -1.2654, 2.6301],
    #          [-0.7569, -0.7500, 1.6805],
    #          [-1.0757, 0.5645, -1.0072]]], grad_fn= < EmbeddingBackward0 >)




    sentences = ["我是你爹", "你是我儿", "你妈是我老婆"]

    word_list = [i for i in "".join(sentences)]
    word_list = list(set(word_list))
    word_dict = {w:i for i, w in enumerate(word_list)}
    number_dict = {i:w for i, w in enumerate(word_list)}
    n_class = len(word_dict)

    model = NNLM()