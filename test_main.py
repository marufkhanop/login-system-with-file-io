import main

def test_login_system():
    # 1. Sign up a fake user for testing
    main.signup_done("testbot", "botpass123")
    
    # 2. Check if the code correctly logs them in
    assert main.match_user_and_pass("testbot", "botpass123") == True
    
    # 3. Check if the code blocks a wrong password
    assert main.match_user_and_pass("testbot", "wrongpassword") == False