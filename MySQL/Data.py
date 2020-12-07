from MySQL import connector as conn

DBconnector = conn.connector(host='127.0.0.1',
                             user='root',
                             password='1324',
                             port=3306)


def getDate(PatientID, machine):
    sql = "SELECT `time` FROM `data_analysis` JOIN `rehabilitation_information`" \
          " where `rehabilitation_information`.`PatientID` = " + PatientID + " AND `rehabilitation_information`.`machine` = '" \
          + machine + "' AND `rehabilitation_information`.`CSVname` = `data_analysis`.`CSVname` "
    return DBconnector.Read(sql)


def getMachineData(PatientID, Machine):
    sql = "SELECT RTmean, RTstd, RTmax, RTmin, FTmean, FTstd, FTmax, FTmin FROM `data_analysis` " \
          "JOIN `rehabilitation_information` WHERE `rehabilitation_information`.`PatientID` = " + PatientID + \
          " AND `rehabilitation_information`.`CSVname` = `data_analysis`.`CSVname` AND `rehabilitation_information`.`machine` = '" + Machine + "'"
    return DBconnector.Read(sql)


def getPath(PatientID, machine):
    sql = "SELECT `CSVpath` FROM `rehabilitation_information` WHERE `PatientID` = '" + PatientID + "' and `machine` = '" + machine + "' LIMIT 1"
    return DBconnector.Read(sql)[0]['CSVpath'][:19]