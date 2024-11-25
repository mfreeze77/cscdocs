# EST4: Writing rules with delays using 4-CU Version 03.00.00.97  

Introduction  

This bulletin informs you of an issue when writing rules using the –Delay command in 4-CU, Version 03.00.00.97.  

# Issue  

When you build your project, the 4-CU will automatically combine and optimize multiple rules written for the same input device into one rule for faster processing by the EST4 control unit. If any of the rules has restore Delay (-Delay or Delay) output command(s), the resulting execution of the combined and optimized rule may not be in the expected sequence during the event restoral operation.  

Example:  

An installer writes the following two separate rules for the same event.  

$@$ Supervisory 'Supervisory Device 1':  +Delay :05 ,  On HIGH '[Branch2]N-02-SLOT-4-AUD-1' , -Delay :07  

$@$ Supervisory 'Supervisory Device 1':  FastBlink .Indicator 'Indicator 1' The expected operation when the supervisory event activates is that the indicator begins flashing immediately, and the audio message starts after 5 seconds. Upon clearing the supervisory event, the indicator should stop flashing immediately and the audio should stop after 7 seconds.  

The issue in this example is that when the supervisory event is restored, instead of the indicator turning off immediately, there is a delay of 7 seconds before both the indicator and the audio shut off.  

# Solution  

To avoid this issue, combine multiple rules for the same input device and output commands with restore Delay (-Delay or Delay) operations into one rule during rule script writing in the 4-CU. Test the rules system operation for the desired outcome.  

# Example:  

The expected result in the rules above is that indicator 1 should turn off immediately. The combined rule configured in the 4-CU should be as follows, which represents an example of the solution for this issue.  

$@$ Supervisory 'Supervisory Device 1':  +FastBlink .Indicator 'Indicator 1'  

, +Delay :05   
, On HIGH '[Branch2]N-02-SLOT-4-AUD-1'   
, -Delay :07   
, -Off .Indicator 'Indicator 1'   {-Off is required for shutting off indicator immediately}  

# Reminder of NFPA 72 testing requirements  

When changes are made to site-specific software, the following shall apply:  

All functions known to be affected by the change, or identified by a means that indicates changes, shall be 100 percent tested.   
In addition, 10 percent of initiating devices that are not directly affected by the change, up to a maximum of 50 devices, also shall be tested and correct system operation shall be verified.   
A revised record of completion in accordance with NFPA standards shall be prepared to reflect these changes.  

Changes to all control units connected to or controlled by the system executable software shall require a 10 percent functional test of the system, including a test of at least one device on each input and output circuit to verify critical system functions such as notification appliances, control functions, and off-premises reporting.  