import subprocess
import json


def i3msg(itype, imsg):
    p = subprocess.Popen(
        [
            "/bin/sh",
            "-c",
            "i3-msg {0} {1}".format(
                "" if not itype else '-t "{0}"'.format(itype),
                "" if not imsg else '"{0}"'.format(imsg),
            ),
        ],
        stdout=subprocess.PIPE,
    )

    output, error = p.communicate()
    return json.loads(output)
