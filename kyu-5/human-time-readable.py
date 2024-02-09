def make_readable(seconds):
    return ("0" + str(int(seconds/(60*60))))[-2::] + ":" + ("0" + str(int(seconds/60%60)))[-2::] + ':' + ("0" + str(int(seconds%60)))[-2::]
