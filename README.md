# Reference JBrowse REST API Implementation

I threw this together for my testing purposes, figured it might be useful to
other people.

Just load up the "data" folder in your JBrowse instance and you should be good to go.

## Example 1

There is a dead simple Python Flask server implementation. You'll need to install flask to run this.

```$
$ pip install flask
$ python api_ref.py
```

And the API will be available on port 5000

## Example 2

In case the flask example was not clear enough, there are some raw JSON files
that serve as an example in the `raw` folder.
