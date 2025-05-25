# Farewell

<p align="center">
    <a href="https://dmschauer.github.io/farewell">
        <img src="img/farewell_icon_white_border.png" style="padding: 0px 10px; width: 100px;"/>
    </a>
</p>
<p align="center">
    <em>
    Simple, unobtrusive script exit notifications.
    </em>
</p>

## Intro

`Farewell` is a basic utility package. It lets you define two functions and calls either one in case of success/failure of the script run.

The intended use case is sending notifications in case of succesful/failed job runs.


## Installation

```python
pip install farewell
```

```python
uv add farewell
```

## Quick examples

### Basic usage

```python
from farewell import on_exit

def on_success():
    print("✅ Everything worked!")

def on_error(error):
    print(f"❌ Failed: {error['type']} - {error['message']}")

on_exit(success_func=on_success,
        error_func=on_error)

# You actual script logic below - completely unchanged!
print("Script running...")

# Uncomment to test error:
# raise ValueError("Test error!")

print("Script finished!")
```

### Usage with a main()

```python
from farewell import on_exit

def setup_notifications() :
    def success_notification():
        print("✅ Everything worked!")
    
    def error_notification(error):
        print(f"❌ Failed: {error['type']} - {error['message']}")

    on_exit(success_notification, error_notification)

def main():
    print("Script running...")
    
    # Uncomment to test error:
    # raise ValueError("Test error!")
    
    print("Script finished!")

if __name__ == "__main__":
    setup_notifications() # could also be called inside main()
    main()
```

### Example with AWS SNS notifications

Also checkout `./examples/sns.py` for a more complete example.

```python
from farewell import on_exit
import boto3

sns = boto3.client('sns')

def notify_success():
    sns.publish(TopicArn="...", Message="✅ Everything worked!")

def notify_error(err):
    sns.publish(TopicArn="...", Message=f"❌ Failed: {err['type']} - {err['message']}")

on_exit(succes_func=notify_success,
        error_func=notify_error)

# You actual script logic below - completely unchanged!
```

## Alternatives

The following achieves the same but doesn't introduce a new dependency.

Although making this library was a nice excercise, I would recommend you to simply do this instead:

```python
def success_notification():
    print("✅ Everything worked!")

def error_notification(error: Exception):
    print(f"❌ Failed: {type(error).__name__} - {str(error)}")

def main():
    print("Script running...")
    
    # Uncomment to test error:
    # raise ValueError("Test error!")
    
    print("Script finished!")

if __name__ == "__main__":
    try:
        main()
        success_notification()
    except Exception as e:
        error_notification(e)

```
