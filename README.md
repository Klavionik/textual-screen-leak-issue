# Textual Screen Leak Issue
A minimal reproducible example of a screen leak issue in Textual.

## Usage
Clone the repo.
```shell
git clone git@github.com:Klavionik/textual-screen-leak-issue.git
```

Create and activate a new venv.

```shell
cd textual-screen-leak-issue
python -m venv venv
source venv/bin/activate
```

Install dependencies.

```shell
pip install -r requirements.txt
```

Run the dev console in a separate terminal tab.
```shell
textual console
```

Run the app in dev mode.

```shell
textual run --dev main:TheApp
```

## How to reproduce
The first screen displays the report of all `Screen` objects in the memory. Switch
back and forth between `FirstScreen` and `SecondScreen` using the `E` key. You'll see
that the number of screens in the memory only increase but never goes down.

If you take a look at the dev console, you'll find no warnings like
`FirstScreen DELETED` that should be printed right before the object is
deallocated from the memory.
