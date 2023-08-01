import pika, json


def upload(f, fs, channel, access):
    try:
        fid = fs.put(f)
    except Exception as err:
        print(err)
        return "internal server error", 500
# parse to required format
    message = {
        "video_fid": str(fid),
        "mp3_fid": None,
        "username": access["username"], # security consideration - work as demo_payload - useWhen download validation
    }
# push operation \ default_config - PERSISTENT_DELIVERY_MODE
    try:
        channel.basic_publish(
            exchange="",
            routing_key="video",
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )
    except Exception as err:
        print(err)
        fs.delete(fid)
        return "internal server error", 500
