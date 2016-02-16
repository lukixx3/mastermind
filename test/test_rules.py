import mastermind.rules as r

ruleset = [{'url': 'http://localhost:8000/',
            'request': {'skip': True},
            'name': 'foo',
            'response': {'body': 'ok200.json',
                         'headers': {'add': {'X-ustwo-intercepted': 'Yes'}}}}]

rule = {'url': 'http://localhost:8000/',
        'request': {'skip': True},
        'name': 'foo',
        'response': {'body': 'ok200.json',
                     'headers': {'add': {'X-ustwo-intercepted': 'Yes'}}}}


def test_urls_one():
    assert r.urls(ruleset) == ['http://localhost:8000/']

def test_urls_none():
    assert r.urls([]) == []

def test_find_by_url_exact_match():
    assert r.find_by_url('http://localhost:8000/', ruleset) == rule

def test_find_by_url_exact_no_match():
    assert r.find_by_url('http://foo/', ruleset) == None


def test_url():
    assert r.url(rule) == 'http://localhost:8000/'

def test_skip_true():
    assert r.skip(rule) == True

def test_skip_false():
    assert r.skip({'request': {'skip': False}}) == False
    assert r.skip({'request': {}}) == False
    assert r.skip({}) == False

def test_delay():
    assert r.delay({'response': {}}) == None
    assert r.delay({}) == None
    assert r.delay({'response': {'delay': 10}}) == 10


def test_status_code():
    assert r.status_code({'url': 'http://foo',
                          'response': {'code': 500}}) == 500

def test_status_code_casted():
    assert r.status_code({'url': 'http://foo',
                          'response': {'code': '500'}}) == 500

def test_body_filename_exists():
    assert r.body_filename(rule) == 'ok200.json'

def test_body_filename_not_exists():
    assert r.body_filename({'url': 'http://foo'}) == None
