# Seq2Seq + Attention

구분: Exploration
복습: No
정리: Yes

- 관련 논문

    [https://arxiv.org/pdf/1409.0473.pdf](https://arxiv.org/pdf/1409.0473.pdf)

- 주요 개념
    1. RNN, LSTM
    2. seq2seq
    3. attention
    4. teacher forcing
- 목차

---

- 아래 내용은 해당 블로그 내용을 바탕으로 작성했습니다.
    - RNN과 LSTM

        [RNN과 LSTM을 이해해보자!](https://ratsgo.github.io/natural%20language%20processing/2017/03/09/rnnlstm/)

        [Understanding LSTM Networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)

## RNN

![Seq2Seq%20+%20Attention%209d4f29a30c29446bb28ec255bdd04b29/Untitled.png](Seq2Seq%20+%20Attention%209d4f29a30c29446bb28ec255bdd04b29/Untitled.png)

RNN 구조 

RNN은 Hidden Node가 방향을 가진 엣지로 연결돼 순환구조를 이루는 인공신경망의 한 종류입니다. 자연어 처리에서 기본적인  모델로 유명합니다. 

RNN에 대한 설명은 추후 CS231N 강의에 나오니까 그때 다시 정리해보겠습니다. Translation에 쓰이는 RNN의 특성을 간단하게 짚고 가면, 

- 입력과 출력을 sequence  길이에 관계없이 받을 수 있어 네트워크 구조가 유연성이 높습니다.
- 노드간 연결된 순환구조 이므로 이전 히든 노드는 현재 노드에서 반영되는 식으로 gradient가 이전 시점까지 계속 고려되어 반영됩니다. 그러다보니, 노드와 노드간에 거리가 멀면(Long term dependency), gradient가 소실되는 현상이 나타납니다. ⇒ "Gradient Vanishing"

이전에 네이버 영화 리뷰 감성 분석을 할 때는 단어들에서 감성점수를 매기는 여러 입력에서 하나의 출력을 냈다면, Translation에서 쓰이는 RNN은 many to many, 즉 다입력 다출력의 구조를 띕니다. 

## LSTM

![Seq2Seq%20+%20Attention%209d4f29a30c29446bb28ec255bdd04b29/Untitled%201.png](Seq2Seq%20+%20Attention%209d4f29a30c29446bb28ec255bdd04b29/Untitled%201.png)

기본적인 LSTM 구조

![Seq2Seq%20+%20Attention%209d4f29a30c29446bb28ec255bdd04b29/Untitled%202.png](Seq2Seq%20+%20Attention%209d4f29a30c29446bb28ec255bdd04b29/Untitled%202.png)

RNN계열 모델로서 앞서 RNN에서의 gradient vanishing 문제를 해결하는 모델 구조입니다. LSTM에서는 Hidden Node뿐만 아니라, Cell state에 대해 제거(forget), 추가하는 연산을 통해 이러한 문제를 해결합니다. 

Basic한 형태에 해당하는 LSTM일 뿐 Cell에 대한 연산은 조금씩 차이가 있습니다. RNN에서 gradient가 소실되는게 문제니까, 메모리 버퍼에 거치듯 초록색 박스에 해당하는 하나의 Cell 상태를 활성화 함수인 tanh를 거쳐 보호, 제어하는 형태로 이해했습니다. 

- 아래 내용은 해당 유투브 강의를 바탕으로 작성했습니다.

    [[딥러닝 기계번역] 시퀀스 투 시퀀스 + 어텐션 모델](https://www.youtube.com/watch?v=WsQLdu2JMgI)

## Seq2Seq

여기까지는 쉽게 이해가 됐지만 아래부터가 난관이었습니다. 흠.. 노드에서도 RNN, LSTM 두개의 모델을 소개하고 있습니다. 그리고 Cotext vector, Dynamic context vector, Encoder, Decoder 등과 같은 개념이 등장합니다. 이러한 개념들이 Seq2Seq에서 어떻게 활용되는지 정리했습니다.

### "Word to Word" translation is not  optimal solution

- 영어와 한국어는 다른 어순을 가지고 있다.
    - 영어: Subject, Verb, Object
    - 한국어: Subject, Object, Verb
- 영어의 단어 개수와 번역한 한국어 단어의 개수가 다른 상황이 있는데 단어 단위로 해석하면 항상 영어, 번역된 한국어가 같은 개수를 가져야 한다.
    - 예시: how are you ? → 잘 지내 ?
- Seq2Seq란?

    입력 문장을 Encoding해줌으로써 벡터로 만들어주고, 만들어진 벡터를 활용해서 다른 도메인(예를 들면, 다른 언어)의 문장으로 출력하는 Decoding하는 딥러닝 아키텍처입니다. 

    - Encoder: 문장을 단어마다 읽어서 Fixed size를 가지는 Context vector를 형성
    - Decoder: Context vector를 번역

### RNN 2개로 구성된 Seq2Seq

기본적인 Seq2Seq는 RNN 2개로 이뤄졌습니다. 여기서 RNN은 CNN처럼 모델 아키텍쳐의 한 종류입니다. RNN 1개는 Encoder 역할을 수행하고, 다른 RNN 1개는 Decoder 역할을 수행합니다. 

1. Encoder에서는 Fixed 입력 문장을 단어 단위로 각 cell을 거쳐 Encoder의 모든 Step에서의 Hidden node(state)를 반영하는 Fixed Context vector를 형성합니다. 
    - Context vector(문맥 벡터):  아래 그림의 네모 형태가 Cell(메모리 공간?)에 해당합니다. Cell에 순차적으로 단어들이 거쳐오면서, 마지막으로 정보를 담고 있는 벡터입니다.
2. Decoder에서는 Encoder를 통해 형성된 Context vector를 전달받아 한 단어씩 생성해냅니다. 
- 예시)

    입력: i → love → you → <start> Nan nul saranhey <end>

    ![Seq2Seq%20+%20Attention%209d4f29a30c29446bb28ec255bdd04b29/Untitled%203.png](Seq2Seq%20+%20Attention%209d4f29a30c29446bb28ec255bdd04b29/Untitled%203.png)

### LSTM 2개로 구성된 Seq2Seq

- RNN과의 차이
    1. LSTM으로 이뤄진 Seq2Seq는 기존 RNN으로 구성했을 때와 차이점은 Hidden state  뿐만 아니라 Cell state도 같이 가지고 간다는 점입니다. 
    2. RNN에서 Long term dependency로 인해 나타나는 gradient vanishing 문제를 개선합니다. 
- Q. RNN계열 Seq2Seq에서 입력 문장이 길어져 단어 개수가 많아진다면?

    문장 사이즈가 작을 땐 괜찮지만, 크게 되면 문맥 벡터는 **Fixed size**를 가지기 때문에  모든 정보를 함축할 수 없는 문제가 발생합니다.

    이러한 큰 입력 문장이 들어오게 되면 RNN계열(Vanila RNN, LSTM, GRU 등)이 가진 gradient vanishing 문제는 더 두드러지게 됩니다. 

    LSTM은 그걸 해결한게 아닌가?라는 의문이 들었지만 RNN은 입력 문장이 엄청 커져서 노드간의 연결이 길어진다면 LSTM도 RNN계열이라 문제를 피할 수 없긴 합니다.  

    이유는 tanh에 있다고 생각했습니다. 활성화 함수를 배울 때, 어떤 함수든 gradient vanishing이 개선될 뿐 정보 손실의 문제는 있었기 때문에 RNN 계열은 어떠한 state를 전달해서 Context vector를 만들 때 정보 손실이 발생한다고 이해했습니다.  

    결국, Encoder의 마지막 Time step에 해당하는 state(RNN: hidden state, LSTM: hidden, cell state)를 Context vector로 활용한다는 점에서 모든 RNN은 입력 Sequence의 정보 손실 문제를 가지고 있습니다. 

    **이러한 문제점의 해결책으로 Attention이 제시됩니다.**

### Seq2Seq with Attention

Fixed Context Vector에 대한 해결책으로 Attention 메커니즘이 제안됩니다.

- 기존 Seq2Seq와 Attentional Seq2Seq의 차이
    1. RNN계열 Seq2Seq는 Fixed Context Vector를 가집니다. 그러나, Attention을 활용하면 softmax 같은 활성화 함수를 거쳐 각 Step의 hidden state 정보를 모두 반영한 Dynamic context vector를 가집니다. 
    2. RNN계열 Seq2Seq는 Encoder의 모든 Hidden state가 동일한 비중으로 반영됩니다. 그러나, Attention 메커니즘을 적용하면 **Decoder의 현재 time step**의 예측에 softmax 함수를 사용해 각 step의 영향력에 따른 가중합(Attention weight)을  전달합니다. 
        - Softmax 함수: 입력받은 값을 0~1 사이의 값으로 정규화합니다. 출력값들의 총합은 항 상 1이 됩니다. 주로 다중 분류 모델에서 사용되는 활성화 함수입니다.

    따라서 기존 RNN 기반의 Seq2Seq와 다르게 마지막 hidden state에  고정된 Context vector를 사용하는 것이 아니기 때문에, Decoder의 현재 step이 어디인지에 따라 context vector는 다른 값을 가집니다. 

- 그림으로 이해하는 Attentioninal Seq2Seq
    1. 마지막 단의 hidden state를 활용하는 Fixed context vector의 단점을 극복하기 위해 encoder의 각 state에 대해 Dynamic(다양하게, 각각의 state별로) context vector를 생성합니다. 

        ![Seq2Seq%20+%20Attention%209d4f29a30c29446bb28ec255bdd04b29/Untitled%204.png](Seq2Seq%20+%20Attention%209d4f29a30c29446bb28ec255bdd04b29/Untitled%204.png)

        Fixed Context Vector와 Dynamic  Context Vector 비교  

    2. 각 state에 대한 context vetor를 추출했으므로 이 중 **집중**하고 싶은 vectors를 선택할 수 있게 됩니. 
        - 예시: i love you에 대한 Seq2Seq with Attention

            Decoder의 현재 Step이 <start>, 난, 널, 사랑해, <end> 중 어느 토큰에 해당하느냐에 따라 Dynamic context vector에 해당하는 cv값이 달라짐을 알 수 있습니다. 

            ![Seq2Seq%20+%20Attention%209d4f29a30c29446bb28ec255bdd04b29/Untitled%205.png](Seq2Seq%20+%20Attention%209d4f29a30c29446bb28ec255bdd04b29/Untitled%205.png)

            ![Seq2Seq%20+%20Attention%209d4f29a30c29446bb28ec255bdd04b29/Untitled%206.png](Seq2Seq%20+%20Attention%209d4f29a30c29446bb28ec255bdd04b29/Untitled%206.png)

            ![Seq2Seq%20+%20Attention%209d4f29a30c29446bb28ec255bdd04b29/Untitled%207.png](Seq2Seq%20+%20Attention%209d4f29a30c29446bb28ec255bdd04b29/Untitled%207.png)

            ![Seq2Seq%20+%20Attention%209d4f29a30c29446bb28ec255bdd04b29/Untitled%208.png](Seq2Seq%20+%20Attention%209d4f29a30c29446bb28ec255bdd04b29/Untitled%208.png)

---

![https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https://www.notion.so/vgrlo/Seq2Seq-Attention-29f35e74c8b0430eb273238b76460b04](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https://www.notion.so/vgrlo/Seq2Seq-Attention-29f35e74c8b0430eb273238b76460b04)