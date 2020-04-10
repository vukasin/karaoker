# karaoker
Karaoker smaaaash videos from YouTube (and make karaokee)

## Install

Just use PIP

```
pip3 install https://github.com/vukasin/karaoker.git
```

If you get permission issues, you can try installing it to a user dir.

```
pip3 install --user https://github.com/vukasin/karaoker.git
```


## Use

First make a list of YouTube videos you want to convert to Karaoke. Here's an example

``` input.txt
https://www.youtube.com/watch?v=M0p_1rVfOpw
```

Next, pass the file to the karaoker

```
karaoker input.txt
```

The resulting files will be stored in your home directory under

```
Music/karaoker/output/
```

An error log is also written and can be found under

```
Music/karaoker/errors.txt
```

