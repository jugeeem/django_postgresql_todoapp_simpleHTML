# TodoList app  [ Django + Postgresql + TailwindCSS ]   

## 概要  
### 1. このアプリについて
- Django + Postgresql + TailwindCSS で作成したTodoListアプリです。
- ユーザー登録、ログイン、ログアウト、TodoのCRUD機能があります。
- TailwindCSSを使用して、レスポンシブ対応しています。
- また、TailwindCSSはCDNを使用しており、デプロイに向きません。

### 2. 作成した目的
2023年6月よりPythonの学習を開始し、同年8月5日に"Python 3 エンジニア認定基礎試験"に合格しました。  
学習した内容を何か形にしたいと考え、DjangoでTodoListアプリを作成しました。

DjangoをでToDoListアプリを作成した意図としては、以下の2点です。
- Djangoの基礎を学習する
    - CRUD処理、ユーザ認証、テンプレート、静的ファイルの扱い方など
- フルスタックエンジニアを目指すため、フロントエンドとバックエンドの両方を学習する

### 3. 使用技術
- Python 3.11.4
- Django 4.2.4
- Postgresql 14.8
- TailwindCSS 3.3.3

### 4. 所感  
#### 4-1. Djangoの学習について
私が過去、プログラミング初学者のときにはPHPを学習していたこともあり、これまでに使ったことのあるフレームワークはLaravelとFuelPHPのみでした。いづれもMVCモデルを採用しており、DjangoのMTVモデルは初めてでした。その点で、Djangoの学習はとても新鮮でした。半面、MTVモデルの理解に時間がかかりました。また、Djangoの公式ドキュメントはとても充実しており、学習にはとても役立ちました。しかし、Djangoの公式ドキュメントの細部になるとまだ日本語かされていない部分が多く、英語の理解が必要でした。今後は、英語の理解力を高めるためにも、英語のドキュメントを読む習慣をつけていきたいと考えています。

#### 4-2. フォーム操作について
こちらは正直な所、現在も理解できているとは言えない状況です。といいますのも、`templates/todo`配下のフォームの表示方法と、`templates/accounts`配下のフォームの表示方法に差異があります。この主な原因は私のフォーム機能の理解不足によるものです。今後は、フォーム機能の理解を深めていきたいと考えています。

#### 4-3. フロントエンドについて
フロントエンドについては、TailwindCSSを使用しました。TailwindCSSを選択した理由として、CSSフレームワークのBootstrapと比較して、より自由度が高いと考えたからです。また、TailwindCSSはCDNを使用しており、デプロイに向きません。今後は、CDNを使用しない方法でTailwindCSSを使用していきたいと考えています。

### 5. 今後の課題
#### 5-1. フォーム操作の理解
まず、最初にあげるべきは上述したように、Djangoにおけるフォーム操作であると考えております。

#### 5-2. テンプレート層の変更
現在のテンプレートはTailwindCSSを用いた作りになっていますが、テンプレートの処理をNextJSに切り替えたいと考えております。理由としては、NextJSを使用することで、フロントエンドとバックエンドの分離を行いたいと考えているためです。また、NextJSはReactのフレームワークであり、Reactを学習することで、フロントエンドの理解を深めたいと考えているためです。また、その他挙げることができる理由としては、NextJSはSSGとSSRの両方に対応しているため、SEO対策にもなると考えているためです。

### 6. 参考文献

- [Django公式ドキュメント](https://docs.djangoproject.com/ja/4.0/)

- [udemy - 【中級者向け・Django4対応】Python/DjangoによるECサイト開発講座（Django3.2系にも対応）](https://www.udemy.com/course/django-ecweb-vegeket/)

- [udemy - 現役シリコンバレーエンジニアが教えるPython 3 入門 + 応用 +アメリカのシリコンバレー流コードスタイル](https://www.udemy.com/course/python-beginner/)

- [delhi09の勉強日記 - DjangoのLOGGINGの設定についてちゃんと勉強した -](https://kamatimaru.hatenablog.com/entry/2020/12/14/020610)

- [Python 入門 - Django フォームにて CSS クラスを設定する方法 -](https://python.keicode.com/django/form-add-class.php)

- [エンジニア大学 - DjangoのデータベースでPostgreSQLを使う -](https://uha-blog.com/python/django-postgresql/)

- [Tailwind CSS - ドキュメント](https://tailwindcss.com/docs)

- [TAILBLOCKS](https://tailblocks.cc/)  
こちらはToDoListアプリのデザインのベースとして使用させて頂きました。

- [Tailwind CSS CDN](https://www.jsdelivr.com/package/npm/tailwindcss)

- [Flowbite](https://flowbite.com/)  
inputタグやbuttonタグのデザインのベースとして使用させて頂きました。


### 7. 謝辞
今回、簡単なToDoListアプリ作成を通して、上に挙げた通り、様々な方による記事やドキュメントを参考にさせて頂きました。この場を借りて、改めて感謝申し上げます。ありがとうございました。  
まだまだエンジニアとして駆け出しである私ではありますが、今後はどのような形であれ、私の経験が誰かの役に立てるように、日々精進していきたいと考えております。

あらためまして、ありがとうございました。

2023年8月27日 南 龍太郎


# TodoList app [ Django + Postgresql + TailwindCSS ]   

## Overview  
### 1. about this app
- This is a TodoList app created with Django + Postgresql + TailwindCSS.
- It has user registration, login, logout, and CRUD functionality for Todo.
- It is responsive using TailwindCSS.
- Also, TailwindCSS uses CDN and is not suitable for deployment.

### 2. Purpose of Creation
I started learning Python in June 2023 and passed the "Python 3 Engineer Certification Basic Exam" on August 5 of the same year.  
I wanted to put what I learned into some form, so I created a TodoList application in Django.

I created the ToDoList app with Django for the following two reasons
- To learn the basics of Django
    - CRUD processing, user authentication, templates, static file handling, etc.
- To learn both front-end and back-end in order to become a full-stack engineer.

### 3. Technologies used
- Python 3.11.4
- Django 4.2.4
- Postgresql 14.8
- TailwindCSS 3.3.3

### 4. impressions  
#### 4-1. Learning Django
In the past, when I was a beginning programmer, I had learned PHP, and the only frameworks I had used were Laravel and FuelPHP. Both of them use the MVC model, and Django's MTV model was new to me. In that respect, learning Django was very refreshing. On the other hand, it took me a while to understand the MTV model. Also, the official Django documentation was very comprehensive and very useful for learning. However, there are many parts of the official Django documentation that are not yet in Japanese, so understanding English was necessary. In the future, I would like to make it a habit to read English documents to improve my English comprehension.

#### 4-2. About form manipulation
To be honest, I cannot say that I still have a good understanding of this area. There is a difference between the way forms under `templates/todo` are displayed and the way forms under `templates/accounts` are displayed. This is mainly due to my lack of understanding of the form function. I would like to deepen my understanding of form functions in the future.

#### 4-3. About the front end
For the front end, we used TailwindCSS. we chose TailwindCSS because we thought it offered more flexibility compared to Bootstrap, a CSS framework. Also, TailwindCSS uses a CDN and is not suitable for deployment. In the future, we would like to use TailwindCSS in a way that does not use a CDN.

### 5. future issues
#### 5-1. Understanding Form Manipulation
The first thing we need to give you is form manipulation in Django, as mentioned above.

#### 5-2. Template layer changes
Our current templates are built using TailwindCSS, but we would like to switch to NextJS for template processing. The reason is that we would like to separate the front end from the back end by using NextJS. Also, NextJS is a React framework, and we would like to deepen our understanding of the front end by learning React. Another reason that can be mentioned is that NextJS supports both SSG and SSR, and we believe that this will help with SEO.

### 6. References.

- [official Django documentation](https://docs.djangoproject.com/ja/4.0/)

- [udemy - [Intermediate level, Django4 compatible] EC Site Development with Python/Django (also compatible with Django 3.2 series)](https://www.udemy.com/course/django-ecweb-vegeket/)

- [udemy - Introduction to Python 3 + Applications taught by a working Silicon Valley engineer + Silicon Valley style of coding in the US](https://www.udemy.com/course/python-beginner/)

- [delhi09's Study Diary - I learned about setting up LOGGING in Django properly -](https://kamatimaru.hatenablog.com/entry/2020/12/14/020610)

- [Introduction to Python - How to set CSS classes in Django forms -](https://python.keicode.com/django/form-add-class.php)

- [Engineer University - Using PostgreSQL with Django's Database -](https://uha-blog.com/python/django-postgresql/)

- [Tailwind CSS - Documentation](https://tailwindcss.com/docs)

- [TAILBLOCKS](https://tailblocks.cc/)  
This one was used as the basis for the design of the ToDoList application.

- [Tailwind CSS CDN](https://www.jsdelivr.com/package/npm/tailwindcss)

- [Flowbite](https://flowbite.com/)  
We used this as a base for the design of input and button tags.


### 7. Acknowledgements
Through the creation of this simple ToDoList application, I have referred to the articles and documents by various people as listed above. I would like to take this opportunity to thank you again. Thank you very much.  
Although I am still a novice engineer, I would like to devote myself every day to making my experience useful to others, in whatever way I can.

Again, thank you very much.

Ryutaro Minami, August 27, 2023