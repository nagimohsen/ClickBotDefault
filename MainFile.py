import selenium
from webdriver import WebDriver
import time
import sys
import sqlite3



class Link_Click(WebDriver):
    def __init__(self):
        pass
    def Load_Data_From(self):
        connection = sqlite3.connect("ProxiesDB.db")  # connect to your DB
        cursor = connection.cursor()  # get a cursor
        '''cursor.execute("SELECT Proxies FROM Proxies_List")  # execute a simple SQL select query
        proxies = cursor.fetchall()
        print(proxies)'''
        jobs = [job[0] for job in cursor.execute("SELECT Proxies FROM Proxies_List")]
        return jobs

        
    #'https://mylocation.org'
    def Start_Bot(self,link,proxy_list,use_proxy,num_clicks=10):
        if num_clicks==0:
            print('Click Amount is 0 So no browsing!!!!')
            return
        print(link,',',proxy_list,',',use_proxy)
        num_successes=0
        flag=False
        if use_proxy:
            while True:
                for proxy in proxy_list:
                    
                    WebDriver.__init__(self,proxy=proxy,use_proxy=use_proxy)
                    for x in range(3):
                        try:
                            self.driver.get(link)
                            self.wait_until_page_loaded()
                            time.sleep(2)
                            body=self.driver.find_element_by_tag_name('body')
                            if 'There is something wrong with the proxy server' in body.text or 'No Internet' in body.text or "This page isn’t working" in body.text or "The Connection has timed out" in body.text or "This site can’t be reached" in body.text :
                                print('\n!!!!!!!!!!!!!!!!!!\nproxy failed in try number # '+str((x+1))+'\n\n'+'Retrying The Proxy --> '+proxy+'\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
                                if x==2:
                                    print('\n:(  :(  :(  :(  :(  :(  :(  :(  :(  \nMax Number Of Retries Reached\nProxy '+proxy+' Failed in all 3 tries\n:(  :(  :(  :(  :(  :(  :(  :(  :(  \n')
                                continue
                            else:
                                print('\n#########################'+'\nSuccess:)-->using proxy  #  '+proxy+'  in try number #  '+str((x+1))+'\n##############################\n')
                                print('\n#############################\nBody When Succeeded : \n'+body.text+'\n#############################\n')
                                num_successes=num_successes+1
                                if num_successes>num_clicks or num_successes==num_clicks:
                                    print('Click Amount Reached!!!!')
                                    self.driver.quit()
                                    return
                            time.sleep(5)
                            break
                        except Exception as e:
                            print(str(e))
                            continue
                    self.driver.quit()


        else:
            num_successes_2=0
            WebDriver.__init__(self,use_proxy=use_proxy)
            while True:
                try:
                    self.driver.get(link)
                    self.wait_until_page_loaded()
                    print('successfully clicked without using proxies')
                    num_successes_2=num_successes_2+1
                    if num_successes_2>num_clicks or num_successes_2==num_clicks:
                        print('Click Amount Reached!!!')
                        self.driver.quit()
                        return
                    time.sleep(2.5)

                except Exception as e:
                    print(str(e))
                    continue


    def Add_Proxy(self,proxy):
        conn = sqlite3.connect('ProxiesDB.db')
        c = conn.cursor()
        c.execute('insert into Proxies_List(Proxies) values (?)', (proxy,))
        conn.commit()


    def RemoveProxy(self,proxy):
        conn = sqlite3.connect('ProxiesDB.db')
        c = conn.cursor()
        c.execute('DELETE FROM Proxies_List WHERE Proxies=?', (proxy,))
        conn.commit()
        c.close


'''conn = sqlite3.connect('ProxiesDB.db')
        curs = conn.cursor()

        sql = "select * from %s where 1=0;" % 'Proxies_List'
        curs.execute(sql)
        print([d[0] for d in curs.description])'''




    


    
