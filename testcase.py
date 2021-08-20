from selenium import webdriver

def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="D:/Programs/chromedriver.exe")
    #driver.maximize_windows();
    driver.get("http://localhost/form.php")

def test_form_entry():

    driver.find_element_by_name("nip").send_keys("123456789")
    driver.find_element_by_name("nama").send_keys("Jon jon")
    driver.find_element_by_name("nik").send_keys("9999999999")
    driver.find_element_by_name("alamat").send_keys("Tangerang")
    driver.find_element_by_name("perusahaan").send_keys("fiktif inc.")
    driver.find_element_by_name("tanggal").send_keys("01/01/2001")
    driver.find_element_by_name("divisi").send_keys("hrd")
    driver.find_element_by_name("posisi").send_keys("staf")
    driver.find_element_by_name("gaji").send_keys("10000000")
    driver.find_element_by_name("atasan").send_keys("gemblung")

    driver.find_element_by_name("submit").click()

def test_cleanup():
    driver.close()
    driver.quit()
    print("test selesai")
