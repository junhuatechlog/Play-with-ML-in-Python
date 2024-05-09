# Shell commands

### Copy 文件到指定目录

```shell
junhuawa@N-20KEPC0Y7KFA MINGW64 /c/N-20KEPC0Y7KFA-Data/junhuawa/Documents/00-MyNotes/coding-169-master/coding-169
$ find . -name "*.pdf"
./01-About-This-Course/Chapter-01-watermarked.pdf
./02-Machine-Learning-Basics/Chapter-02-watermarked.pdf
./03-Jupyter-Notebook-Numpy-and-Matplotlib/Chapter-03-watermarked.pdf
./04-kNN/Chapter-04-watermarked.pdf
./05-Linear-Regression/Chapter-05-watermarked.pdf
./06-Gradient-Descent/Chapter-06-watermarked.pdf
./07-PCA-and-Gradient-Ascent/Chapter-07-watermarked.pdf
./08-Polynomial-Regression-and-Model-Generalization/Chapter-08-watermarked.pdf
./09-Logistic-Regression/Chapter-09-watermarked.pdf
./10-Classification-Performance-Measures/Chapter-10-watermarked.pdf
./11-SVM/Chapter-11-watermarked.pdf
./12-Decision-Tree/Chapter-12-watermarked.pdf
./13-Ensemble-Learning-and-Random-Forest/Chapter-13-watermarked.pdf

junhuawa@N-20KEPC0Y7KFA MINGW64 /c/N-20KEPC0Y7KFA-Data/junhuawa/Documents/00-MyNotes/coding-169-master/coding-169
$ find . -name "*.pdf" -exec cp {} ../ppts/ \;
```