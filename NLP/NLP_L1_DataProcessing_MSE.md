`해당 정리노트는 Wikidocs 딥러닝으로 배우는 자연어처리 입문과 AIFFEL 대전의 학습자료를 기반으로 정리했음을 밝힙니다.`

# NLP. Data preprocessing     

## Lecture1. 텍스트 데이터 다루기 
* **전처리(Preprocessing): Natural language에서 Noise, Regex(정규표현식)**
* 표현(Representation): 희소 표현, 분산 표현
* Representation 관련 논문: [Subword-level Word Vector Representations for Korean](https://www.aclweb.org/anthology/P18-1226.pdf)
* 해당 논문 리뷰: https://brunch.co.kr/@learning/7
* 유사도 기법: 코사인 유사도  
* 맥락: 단어 표현에서 맥락 표현까지 
* 토큰화 기법: 공백(주로, 영어), 형태소(한국어), OOV
* Wordpiece Model(WPM): Byte Pair Encoding(BPE)에서 WPM
* BPE 관련 논문: [Neural Machine Translation of Rare Words with Subword Units](https://arxiv.org/pdf/1508.07909.pdf)
* WPM 관련 논문: [JAPANESE AND KOREAN VOICE SEARCH] (https://static.googleusercontent.com/media/research.google.com/ko//pubs/archive/37842.pdf)
* 임베딩 기법: Word2Vec, CBOW, Skip-gram, FastText, ELMo, BERT

## [Wikidocs](https://wikidocs.net/22660)
* **텍스트 전처리**
  - Tokenization 
  - Stemming and Normalization
  - Stemming and Lemmatization
  - Stopword
  - Regular Expression
  - Integer Encoding 
  - Padding 
  - One-hot encoding 
  - Splitting data 
  - Text preprocessing Tools for Korean text
* 언어 모델
  - Language Model 
  - Statistical Language Model(SLM, 통계적 언어 모델)
  - N-gram 
  - Language Model for Korean Sentences 
  - Perplexity
  - Conditional Probability 
---
### Tokenization 

#### Text data
* Corpus: 정제되지 않은 말뭉치
* Token: 최소 단위
	- 상황따라 최소 단위의 기준은 달라질 수 있다. e.g. 영어: 단어, 한국어: 형태소
	- 문장도 Token이 될 수 있다. 
* Punctuation(구두점): . , ? ; !
* Whitespace(띄어쓰기): 단어가 토큰일 때 데이터 전처리단에서 seperator/boundary(분리자/구분자)로 많이 사용
   
#### Tokenization is ... 
* Corpus to Token 
  
#### Tokenizer
* NLTK: for English e.g. Don't => 'Do', "n't"
* WordPunctTokenizer: for English e.g. Don't => 'Don', "'", 't'
* text_to_word_sequence in Tensorflow.keras.preprocessing e.g. Don't => Don't 

#### Standard Tokenizer
* TreebankWordTokenizer: Penn Treebank Tokenization
	- 규칙 1. hypen으로 구성된 단어는 하나로 유지한다.
	- 규칙 2. doesn't와 같이 아포스트로피로 '접어'가 함께하는 단어는 분리해준다.

#### Difficulty in Korean tokenization 
* 교착어이다. 어절이 독립적인 단어로 구성된 영어와 달리, 조사나 다른 무언가가 붙어있는 경우가 많다. 
* 띄어쓰기가 잘 키져지지 않는다. 띄어쓰기 없이도 문장 이해가 가능해서 띄어쓰기가 틀릴 때가 많다. 
* Part-of-speech tagging(품사태깅)의 어려움: 품사에 따라 단어 의미가 달라질 수 있다. e.g. 망치와 '못', '못'하다. 

#### Morpheme(형태소) Tokenizer in Korean 
* Okt
* Mecab: less time
* Komoran
* Hannanum
* Kkma

### Cleaning and Normalization 
* Cleaning: Corpus에서 Noise를 제거한다. 
  - 불필요한 단어 제거 e.g. 특수문자
    * 등장 빈도가 적은 단어 
    * 길이가 짧은 단어 
    * 정규표현식 e.g. HTML 태그 제거 
* Normalization: 표현 방법과 다른 단어들을 통합시켜서 같은 단어로 만들어준다.
  - Stemming and Lemmatization(어간 추출과 표제어 추출)
  - 대소문자 통합

### Normalization 

#### Stemming and Lemmatization(어간 추출과 표제어 추출)
* Stemming(어간 추출) e.g. 영어 - Porter 알고리즘
  - 사전에 없는 단어들이 포함될 수 있다.
  - Lemmatization 보다 일반적으로 빠르다.  
* Lemmatization(표제어 추출): 뿌리 단어를 찾는 것 e.g. am/are/is의 표제어 - be, 형태소 
  - 형태소: stem(어간)과 affix(접사) e.g. NLTK의 WordNetLemmatizer
  - 표제어 추출기는 본래 단어의 품사 정보를 알아야만 정확한 결과를 얻을 수 있다. 
* Stemming과 Lemmatization의 차이점: Stemming은 POS(품사 정보)가 보존되지 않고 Lemmatization은 품사 정보를 보존합니다. 
  
#### 한국어 Stemming 
|언|품사|
|--|--|
|체언|명사, 대명사, 수사|
|수식언|관형사, 부사|
|관계언|조사|
|독립언|감탄사|
|**용언**|**동사, 형용사**|
* 활용: 용언의 어간 + 어미
  * 규칙 활용
  * 불규칙 활용

#### Stopword(불용어)
큰 의미 없는 단어 토큰을 제거 e.g. NLTK 활용 
* 



