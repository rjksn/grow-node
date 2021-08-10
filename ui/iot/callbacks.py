import paho.mqtt.client as mqtt

def error_str(rc):
    """Convert a Paho error to a human readable string."""
    return '{}: {}'.format(rc, mqtt.error_string(rc))

def on_connect(unused_client, unused_userdata, unused_flags, rc):
    """Callback for when a device connects."""
    print('on_connect', mqtt.connack_string(rc))

    # After a successful connect, reset backoff time and stop backing off.
    global should_backoff
    global minimum_backoff_time
    should_backoff = False
    minimum_backoff_time = 1

def on_disconnect(unused_client, unused_userdata, rc):
    """Paho callback for when a device disconnects."""
    # Aug 10 01:24:30 pigrow gunicorn[5259]: on_disconnect 0: No error.
    print('on_disconnect', error_str(rc))

    # Since a disconnect occurred, the next loop iteration will wait with
    # exponential backoff.
    global should_backoff
    should_backoff = True

def on_publish(unused_client, unused_userdata, unused_mid):
    """Paho callback when a message is sent to the broker."""
    print('on_publish')

def on_message(unused_client, unused_userdata, message):
    """Callback when the device receives a message on a subscription."""
    payload = str(message.payload.decode('utf-8'))
    print('Received message \'{}\' on topic \'{}\' with Qos {}'.format(
            payload, message.topic, str(message.qos)))

def on_log(unused_client, unused_userdata, message):
    """Callback when ___."""
    print('on_publish')
    # payload = str(message.payload.decode('utf-8'))
    # print('Received log \'{}\' on topic \'{}\' with Qos {}'.format(
    #         payload, message.topic, str(message.qos)))

def on_unsubscribe(unused_client, unused_userdata, unused_mid):
    """Paho callback when ___."""
    print('on_unsubscribe')

def create_callback():
    callbacks = {
        'on_message' : on_message,
        'on_connect' : on_connect,
        'on_disconnect' : on_disconnect,
        'on_publish' : on_publish,
        'on_message' : on_message,
        'on_unsubscribe' : on_unsubscribe,
        'on_log' : on_log,
    }
    return callbacks
