import csv, re, os, time
os.system('cls')        # clears screen
start_time = time.time()

input_file = "input.csv"
output_file = "output.csv"
input_array = []
output_array = []
date_table = {}

header = {
    "1": ["[OPERATOR]","userId","undeterminedEndDate","recurrenceGroup.externalCode","startTime","endTime","timeType.externalCode","startDate","endDate","approvalStatus","quantityInDays","quantityInHours","workflowRequestId","cancellationWorkflowRequestId","fractionQuantity","editable","loaStartJobInfoId","loaEndJobInfoId","loaExpectedReturnDate","loaActualReturnDate","flexibleRequesting","deductionQuantity","externalCode","workflowInitiatedByAdmin","displayQuantity","cust_TimePeriod.externalCode"],
    "2" : ["'Supported operators: Delimit, Clear and Delete'","User","Undetermined End Date(Valid Values : TRUE/FALSE)","Employee Time Group.externalCode","Start Time","End Time","Time Type.External Code","Start Date","End Date","Approval Status(Valid Values : PENDING/CANCELLED/APPROVED/REJECTED/PENDING_CANCELLATION   PENDING for Pending  CANCELLED for Canceled  APPROVED for Approved  REJECTED for Declined  PENDING_CANCELLATION for Cancellation Pending  )","Number Of Days","Number Of Hours","Workflow Request","Cancellation Workflow Request","Fraction Quantity","Editable(Valid Values : TRUE/FALSE)","Leave Of Absence Job Info ID (Start)","Leave Of Absence Job Info ID (Return To Work)","Expected Return Date","Actual Return Date","Flexible Requesting(Valid Values : TRUE/FALSE)","Deduction Quantity","External Code","Workflow Initiated By Admin(Valid Values : TRUE/FALSE)","displayQuantity","Picklist Value.External Code"]
}

# process input file
def load_input():
    try:
        with open(input_file, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)
            next(csvreader)
            next(csvreader)
            temp = next(csvreader)  # line with dates
            count = 0               # column number
            for i in temp:
                if count > 17:
                    date_table[count] = i
                count += 1

            for i in date_table:
                print(i, ":", date_table[i])

            print
            # print("alpa test")
            for row in csvreader:
                input_array.append(row)
    except:
        input("Input file error. Press Enter to try again or Ctrl+C to exit.")

# process output file
def load_output():
    print("loading output")
    try:
        with open(output_file, 'w', newline="") as resultFile:
            wr = csv.writer(resultFile, delimiter=',')
            wr.writerow(header["1"])
            wr.writerow(header["2"])
            for row in output_array:
                wr.writerows([row])
    except:
        input("Output file generation failure. Press Ctrl+C to quit.")

# process RPTO stuff
def process_me():
    print("Processing Date... beep boop beep")

    for row in input_array:
        count = 0
        for i in row:
            print("i:",i)
            if i == "1":
                print("appending a 1")
                output_array.append(["",row[0], "FALSE", "", "", "", "RTO", date_table[count], date_table[count], "APPROVED", "1", "8", "","","8","TRUE","","","","","FALSE","8","","FALSE","","No_selection"])
            elif i == "0.5":
                print("appending a 0.5")
                output_array.append(["",row[0],  "FALSE", "", "", "", "RTO", date_table[count], date_table[count], "APPROVED","0.5", "4", "","","4","TRUE","","","","","FALSE","4","","FALSE","","No_selection"])
            else:
                print("print nothing")
            count += 1



if __name__ == "__main__":
    print("\nBegin program.")
    load_input()
    process_me()
    load_output()

    # Time to complete process
    time_amount = "%.2f" % ((time.time() - start_time))
    print("Basic --- Time in seconds: ---", time_amount)
