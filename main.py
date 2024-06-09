from chef_mq import instant


def handle_message(ch, method, properties, body):
    print(body.decode("utf-8"))


if __name__ == "__main__":
    instant.consume(channel_name="doorman_to_chairman", cb=handle_message)
