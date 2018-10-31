# NLP Course Project
Elaboration on NLP tasks for Shahid Beheshti University
In this repository we will be specifying the course project guidelines and also finally once all projects are done, make the project available to public as opensource project. 
This project is part of NLP course in [Shahid Beheshti University](http://sbu.ac.ir). For more information on the NLP projects you can look at [NLP Lab Website.] (http://nlp.sbu.ac.ir/). 

Items that this project will cover

#Tasks 
For each of the below tasks there is an input and output format that needs to be defined. It is preferred that the formats to be unified to make more use of data in different tasks. 

# Input File
In this task the input will be a plain text file (.txt) It will be UTF-8 encoded and can be very large (up to giga bytes).

# Output File
## Normalization 
Normalization is the basic step of this competition. We are not going to score your normalizations, but if you don't properly normalize the processed text then, you might lose some score as our scoring algorithm relies on word match.  So here are some of the know normalizations that you must perform: 
* All Arabic characters must be converted to corresponding Persian one (ک ی ه أ ...)
* The only acceptable Zero-width space (نیم فاصله) is U+200C
* ...
* 

## File Format
With each input file the tools must produce a file with same name but a different  extension (.out)
The (.out) file is a tab(\t) delimited format.  Each line of the file starts with the token that is identified. The format is based on CONLL file format.  Here is the columns of the file: 
1. Index of the token in the sentence. Starting from 0 
2. Normalized word form which is the result of the Tokenization and Normalization
3. Stem of the token from stemmer 
4. Lemma of the token  from the Lemmatizer 
5. Morphological Structure of the token. Once the morphemes are detected the have to be concatenated by ```+``` character. If there are multiple morphological structures then you can separate them with ```|``` character 
6. Morphological Analysis of the token. The number of elements in analysis column should be equal to the number of elements in Morphological structure column (separate by ```|```) Use the tokens mentioned [Here](#Morphological-Analysis).

If a token is punctuation or your tool does not produced a value for specific column make sure that you will be leaving a ```_``` in the that column. Except for end of sentence each line must have 6 tabs characters (\t). An empty line means end of a sentence.  

The whitespaces between the tokens should be ignored. (you must include them if they are in middle of the detected tokens). Following characters are considered white spaces: 
* \r
* \n 
* \t
* Normal Space

All other characters are considered to be tokens if not part of another token. 
For example for following sentence: 

> Sample file will be placed in the repository soon 

#  Reference File 
The test file will contain the same format file as output but with (.ref) extension. This file is the evaluation benchmark for the output file produced. 

# Tokenization & Segmentation

## Evaluation Method 
For tokenization task based on the ref file that is provided, we will find the largest number of common lines between the output file and the reference file. 
The total score will be the sum of the scores you get from all input samples. 

For segmentation purpose, we do as following. One sentence tokens (until the empty line) are concatenated and any further whitespace will removed as well. Then we will count the number of matches between the sentences in the reference file and output file. 

## Morphological Analysis 
For morphological analysis the possible tag values are as follows. If your tool is not as complete to produce all detailed tag  you can produce a simple tag (you will get  partial score though). 

|Tag | Value | Partial Tag |
|----|-------|----|
|A0|صفت|A|
|A1|صفت اشاره|A|
|A2|صفت مبهم|A|
|Ab|اختصارات|A|
|Ad|قید|A|
|Al|حروف الفبا|A|
|C0|حرف ربط|C|
|C1|حرف ربط گروهی|C|
|Exp|عبارت|Exp|
|Intj|صوت|Intj|
|N1|اسم|N|
|N2|اسم خاص مکان |N|
|N3|اسم خاص اشخاص|N|
|N4|اسم فامیل|N|
|N5|ضمیر فاعلی|N|
|N6|ضمیر اشاره|N|
|N7|ضمیر تاکیدی انعکاسی|N|
|N8|ضمیر مشترک  متقابل|N|
|N9| اسم موجود در ساختمان حرف اضافه و حرف ربط گروهی|N|
|NA|ضمیر پرسشی|N|
|No|عدد|No|
|Nu|عدد اصلی|No|
|Po|حرف اضافه پسین|P|
|Pr|حرف اضافه|P|
|Pr1|حرف اضافه گروهی|P|
|Si|علامت|S|
|Sp|شاخص|S|
|V1|بن مضارع|V|
|V2|بن ماضی|V|
|V3| فعل اسنادی|V|
|V4|فعل وجه نما|V|
|V5|فعل کمکی|V|
|V6|فعل امر|V|
|VPr | پیشوند فعل|VPr|
|Pl| علامت جمع| Pl| 
|Y|  حرف ی| Y| 
|Neg| علامت نفی|Neg|
|O| هر گونه وندی که در دسته های قبل نبود|O|


# How to participate 
This is a multi phase competition and the aim is to build a good test and evaluation set at the end. We also promote open-source culture to re-use each other's achievements. 
## Phase I: Write your code
Prepare your code and make it ready. Use whatever tool that you like. But consider the fact that you should be able to use your scripts on many files (each group will come up with a brand new test file) . At this stage there is no language or technology preference. But if we want to get something out of this competition we can put an standard on the language that is used. 

Based on the defined format you can start your work, upon release of this document. 

## Phase II: Prepare your test files 
Each group should write a test file. In one day every group is responsible to upload their input files to repository inside data folder. 
You should be able to use **GIT** to upload your files into repository.  Please read about GIT if you don't know already. You must create pull requests to the repo, in order to push data. Approvers will review your pull request and might give you some feedback if necessary.  

Each team will have a dedicated folder.  The folder name must be your team name. You are free to choose a name for your team. You must leave a **Readme.md** file in your folder and write your team member names and some sort of communication method (preferably email). 

The input file name must be **Your_Team_Name.txt** 

## Phase III: Run your code 
Download all of the input files and run your code on them.  Then upload your results back to the repository. Use pull requests as mentioned above. Your output files must be stored in your own folder and the file name should be the same as the input file but with **.ref** extension. 

> Please note that you should run your code on all other teams' input files as well. 

## Phase IV: Upload the reference files 

Upload the reference files to the repository. The file name must be **Your_Team_Name.ref** 
Then we run our scoring algorithm on it and will announce the results. 

## Phase V: Upload your code 

Upload the code and scripts that you had to the repository. Also you have to write a small documentation for your code on how to run it and what method it uses.
You must also document the method and the tools that you have used. Please use the **Readme.md** file in your folder. If you don't know how to write a markdown search it in google. Easy!


# Ethics 
We want to promote the open science culture and one of the main points for it is maturity and responsibility. So please make sure that whatever is uploaded is your own work. Even if you use an open source library please mention it on your documentation. Also uploaded results MUST be output of your program and no manual edition is accepted. 
If any violation of a fair competition is detected the matter will be reported to the instructor. 

# Q&A 
**What language we can write our code in?**  You are free to use any language. We strongly suggest python language so for future we can consolidate your code. 

**How should I upload files to this project?**  You should use Git. If you are not familiar with Git, search internet and learn the basics. 

**How I can ask my questions and clarify?** Please open an issue in this project and we will discuss it. here is the link for it [Create a New Issue](https://github.com/sehsanm/sbunlpcourse/issues/new).
