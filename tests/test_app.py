from playwright.sync_api import Page, expect
from lib.peeps_repo import PeepRepository, Peep 
from datetime import datetime
import pytest


#///////// Test GET Route ////////
"""
When: I send a get request to /
Then: I am sent to the home page
"""
def test_get_index(page, test_web_address):
    page.goto(f"http://{test_web_address}/")
    response = page.request.get(f"http://{test_web_address}/")

    expect(response).to_be_ok()


"""
When: I send a get request to /sign_up
Then: I am sent to the sign up page
"""
def test_get_sign_up(page, test_web_address):
    page.goto(f"http://{test_web_address}/sign_up")
    response = page.request.get(f"http://{test_web_address}/sign_up")

    expect(response).to_be_ok()


"""
When: I send a get request to /make_post
Then: I am sent to the sign up page
"""
def test_get_make_post(page, test_web_address):
    page.goto(f"http://{test_web_address}/make_post")
    response = page.request.get(f"http://{test_web_address}/make_post")

    expect(response).to_be_ok()



"""
When: I make a post
Then: the post is added to the timeline
"""
@pytest.mark.skip("Obselete")
def test_make_post(page, test_web_address, db_connection):
    page.goto(f"http://{test_web_address}/")

    # test redirected to /make
    page.click('text=Make a Post')
    page.fill("input[name='content']", "My first peep")
    
    # test redirected to /
    page.locator("[type=submit]").click()

    post = page.locator('p').all()
    print(page.content())
    expect(post[0]).to_have_text("My first peep")

"""
When: I send a post request to /
And: complete a post form
Then: the new post is added to the database
"""
def test_make_post(page, test_web_address, db_connection):
    db_connection.seed('seeds/test_chitter.sql')
    repo = PeepRepository(db_connection)
    page.goto(f"http://{test_web_address}/")

    # test redirected to /make
    page.click('text=Make a Post')
    page.fill("input[name='content']", "The moon was so big tonight")
    #page.fill("input[name='username']", "Caesar")
    #page.fill("input[name='time_posted']", "2023-11-01 15:25:43")
    
    # test redirected to /
    page.locator("[type=submit]").click()
    print(page.content())

    peeps = repo.all()
    assert peeps[-1] == Peep(12, "The moon was so big tonight", datetime(2023, 11, 1, 15, 25,43), None)

    post = page.locator('h4').all()
    
    expect(post[0]).to_have_text("My first peep")
    expect(post[-1]).to_have_text("The moon was so big tonight")

"""
When: I send a request to reverse the order of the peeps
Then: I should be returned a all peeps in reverse order
"""
@pytest.mark.skip('function not set up')
def test_reverse_chronological_order(page, test_web_address, db_connection):

    page.goto(f'http://{test_web_address}/')
    response = page.request.get(f'http://{test_web_address}/')
    expect(response).to_be_ok()

    page.click('text=Reverse order')

    peeps = page.locator('h4').all()

    expect(peeps[0]).to_have_text('Someone save me from this uni lecture')
    expect(peeps[-1]).to_have_text('My first peep')
