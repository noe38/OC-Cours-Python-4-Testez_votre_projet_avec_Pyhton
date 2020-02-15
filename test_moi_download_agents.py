import program.download_agents as script

import urllib.request

from io import BytesIO
import json

# get_agents()

def test_http_result(tmpdir, monkeypatch):
    results = [{
        "age": 84,
        "agreeablness": 0.74
    }]

    def mockretrun(request):
        return BytesIO(json.dumps(results).encode())

    monkeypatch.setattr(urllib.request, 'urlopen', mockretrun)

    p= tmpdir.mkdir('program').join('agents.json')

    script.main(["--dest", str(p), "--count", "1"])

    local_res = json.load(open(p))

    assert local_res == script.get_agents(1)

# main()