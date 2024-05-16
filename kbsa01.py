import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException




import time

def find_and_click_element(driver, element_id, timeout=10):
    try:
        wait = WebDriverWait(driver, timeout)
        element = wait.until(EC.presence_of_element_located((By.ID, element_id)))
        element.click()
    except NoSuchElementException:
        print(f"요소를 찾을 수 없습니다: {element_id}")
    except TimeoutException:
        print(f"요소를 찾는데 시간이 초과되었습니다: {element_id}")
    except ElementNotInteractableException:
        print(f"요소를 클릭할 수 없습니다: {element_id}")
    except Exception as e:
        print(f"알 수 없는 예외가 발생했습니다: {e}")

id = 'emma1130'
password = '11month30th!'

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get("https://kbsa.or.kr/")
# driver.implicitly_wait(3)
driver.maximize_window()



#로그인
find_and_click_element(driver, 'mainframe.VFrameSet.TopFrame.form.div_top.form.btn_login:icontext')
time.sleep(5)
# ID와 비밀번호 입력
driver.find_element(By.ID, 'mainframe.VFrameSet.WorkFrame.form.div_work.form.EdtId').click()
driver.find_element(By.ID, 'mainframe.VFrameSet.WorkFrame.form.div_work.form.EdtId:input').send_keys('emma1130')
# username_input.send_keys(id)
time.sleep(3)

driver.find_element(By.ID, 'mainframe.VFrameSet.WorkFrame.form.div_work.form.EdtPass').click()
driver.find_element(By.ID, 'mainframe.VFrameSet.WorkFrame.form.div_work.form.EdtPass:input').send_keys('11month30th!')
# password_input.send_keys(password)
time.sleep(3)

# 로그인 버튼 클릭
driver.find_element(By.ID, 'mainframe.VFrameSet.WorkFrame.form.div_work.form.BtnLogin').click()
# login_button.click()
time.sleep(10)

#대회/리그
find_and_click_element(driver, 'mainframe.VFrameSet.TopFrame.form.div_top.form.div_Menu.form.btn_menu0:icontext')
#기타리그
find_and_click_element(driver, 'mainframe.VFrameSet.WorkFrame.form.div_menu.form.div_menu4_1.form.btn_6:icontext')
#수도권3조 일정
find_and_click_element(driver, 'mainframe.VFrameSet.WorkFrame.form.div_work.form.grdList.body.gridrow_2.cell_2_6.cellbutton')
#3/16 태그업vs비바
find_and_click_element(driver, 'mainframe.VFrameSet.WorkFrame.form.div_work.form.tabTeam.tab0.form.grdList.body.gridrow_5.cell_5_9.cellbutton')


time.sleep(10)
