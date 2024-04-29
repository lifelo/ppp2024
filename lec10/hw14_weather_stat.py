import sys
if "./" not in sys.path:
sys.path.append("./")

from lec09 import hw_submission

def main():
    URL = "https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do?fileType=csv&pgmNo=70&menuNo=432&serviceSe=F00101&stdrMg=99999&startDt=19040101&endDt=20240422&taElement=MIN&taElement=AVG&taElement=MAX&stnGroupSns=&selectType=1&mddlClssCd=SFC01&dataFormCd=F00501&dataTypeCd=standard&startDay=19040101&startYear=1904&endDay=20240422&endYear=2024&startMnth=01&endMonth=12&sesnCd=0&txtStnNm=%EC%A0%84%EC%A3%BC&stnId=146&areaId=&gFontSize="
    filename = "./jeonju_all.csv"
    download(filename, URL)

    # tmax, tmax_dates = ????
    # tdiff_max, tdiff_max_date = ????

    tmax, tmax_dates = 38, "2021-08-12"
    tdiff_max, tdiff_max_date = 28.5, "1989-01-09"

    hw_submission.submit("홍길동", tmax, tmax_date, tdiff_max, tdiff_max_date)




if __name__ == "__main__":
    main()