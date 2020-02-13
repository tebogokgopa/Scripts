
SFHO_STATUS_REJECTED = 'Rejected'


def addProgressLine():
    pass

def processFault(fault):
    fault['action_Type'] = '<null>'
    for progressLine in progressLines[0]:
        
        if not progressLine.type in ('Attend'):
            continue
        fault['action_Type'] = progressLine.type
        break
	
    if fault['action_Type'] == 'Attend' and fault['servType'].str in ('FTTH','Broadband Voice'):
        print 'Auto Dispatch : Aborted, Condition has been attended before'
        addProgressLine(fault,'Comment',3001, 'Auto Dispatch : Aborted, Condition has been attended before')
        print 'Abort Auto Dispatch comment added to progress lines'
        return (SFHO_STATUS_REJECTED,'Auto Dispatch : Aborted, Condition has been attended before')
