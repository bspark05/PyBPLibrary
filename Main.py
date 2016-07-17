'''
Created on 2016. 7. 17.

@author: Administrator
'''
import FileIO.Excel as excel

if __name__ == '__main__':
    result = excel.excelRead("200603SaleApartment.xlsx", "Seoul", fromRow=4)
    print len(result)
    
    excel.excelWriteOnExistingFile("test.xlsx", "Sheet1", 'A', result, woFirst=0)
    
#     print type(result[0][0])
#     print type(result[1][0])