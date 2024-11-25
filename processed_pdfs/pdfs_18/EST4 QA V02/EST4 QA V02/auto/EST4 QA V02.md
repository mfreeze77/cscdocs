# EST4 Questions & Answers  

# Introduction  

Following are some frequently asked questions that have been received since the August 2019 EST4 release.  Please refer back to the Application Notes section in the my-eddie website for future additions and updates to this document.  

# EST4 Q&A:  

Q:  Where can I find a guide with all the EST4 part numbers?  

A:  Go to my-eddie, Resources & Training>Submittal Guides and download the EST4 Submittal Guide.  This guide is a great resource that includes all the EST4 system components with descriptions and photos in one document.  

Q:  Where can the 4-CPU be mounted?  

A:  Same as the EST3 3-CPU3, the main EST4 4-CPU must be mounted in the first two slots of the 3-CHAS7 with 3-PPS/M main power supply behind it.  

Q:  Is an additional CPU required to support a second LCD in a cabinet?  

A:  Yes, a 4-ANNCPU is required to support the 4-LCDAUDTEL display that is used for firefighter phone operation.  This LCD display can be programmed to show only the remote fire phone call-ins, capable of answering and disconnecting calls.  One important thing to remember is that if a 4-FT or 4-MIC is mounted to the right of the 4- LCDAUDTEL, the 4-ANNAUDTEL card is required.  This small card plugs onto the 4- ANNCPU and converts the analog signal from the –FT or –MIC to digital, making it available to other CPUs and the audio network.  

Q:   If a second CPU in a single cabinet is required, is an additional power supply required?  

A:  No.  You can have only one main CPU in a cabinet.  Additional CPUs such as 4- ANNCPU does not require a separate power supply.  It derives its operating power thru the USB cable connection to the main 4-CPU.  

Q:  How does the 4-ANNCPU that’s needed to support the 4-LCDAUDTEL get mounted?  

A:  The 4-ANNCPU must be behind the 4-LCDAUDTEL display for the ribbon cable interconnection, so if you have a second chassis in the cabinet, it can be mounted to the back of the 3-CHAS7 with 4BRKT-CB (CB $=$ chassis back) bracket.  If you don’t have the second chassis, it can be mounted on the 4-MPLT mounting plate.  The 4–MPLT takes up an entire chassis location in a cabinet, no additional brackets are required to mount the 4–ANNCPU to it  

Q:  What’s the part number to mount a CPU to the side of a chassis?  

A:  4-BRKT-CS ( $\mathrm{{CS}=}$ chassis side)  

Q:  What’s the part number for the cable required if I have led switch cards only (no LCD) on the EST4 inner door frame assembly)?  

A:  4-CABL0542.  This is the only 4-CABLx series flex cable that needs to be ordered separately.  It is used to connect the 4-CPU or 4-ANNCPU to the UI (user interface) rail when no 4-LCD or 4-LCDAUDTEL is installed.  The cables to interconnect the UI rails on the 4-CAB16D and 4-CAB24D inner doors are included.  

Q:  What’s the part number for the UL Listed USB able to interconnect CPUs in a cabinet?  

A:  The 4-CABLUSBSM  USB cable comes included with all “other” CPUs (4-ANNCPU, 4-NET-AD, 4-FWAL), so no need to order separately.  In the event that you want to mount up to the max of three CPUs in one cabinet, you may need to order 4-   
CABLUSBLG USB (long) cable (if one is to be mounted at the bottom of a CAB21, for example)   
The 4-CABLUSBSM is 2.46 ft. (0.75 meters) long.   
The 4-CABLUSBLG is 4.27 ft. (1.3 meters) long.  

# Q:  What are the part numbers of all the optional mounting brackets and plates?  

A:  4-BRKT-CB mounting bracket, chassis, back 4-BRKT-CS mounting bracket, chassis, side 4-MPLT Mounting plate, chassis or battery space Q:  Which parts count as a “node” on the EST4 network?  

A:  There are five components that count as nodes on the (current) 80 node EST4   
network:   
4-CPU   
4-ANNCPU   
4-NET-AD   
4-FWALx   
4-CPUGRPH  

Q:  Does the 4-CPU include alarm, trouble, and supervisory contacts?  

A:  No it does not.  Optional 4-COMREL must be ordered separately if aux contacts are required.  The 4-COMREL mounts to the back of the 4-CPU.  

Q:  CDR-3 coder and PT-1S printer requires a 4-USBHUB.  Is a 4-FWALx required to support it?   
A:  A 4-USBHUB can connect directly to any CPU (4-CPU, 4-ANNCPU, 4-NET-AD, 4- FWAL, 4-CPUGRPH).  

Q:  Does 4-LCDANN get used with all remote annunciators?  

A:  No. The only difference between the 4-LCDANN and 4-LCDLE assemblies is the cable.  4-LCDANN comes with a 4-CABL0504 cable, 4-LCDLE comes with a 4- CABL0502 cable.  

The 4-2ANN assembly includes the 4-LCDANN For 4-4ANN and 4-6ANN, 4-LCDANN is ordered separately.  

For all others (4-8ANN, 4-16ANN, 4-24ANN, 3-CAB5B/7B,14B), the 4-LCDLE is ordered separately.  

Q: When is the 4-AUDTELS or 4-ANNAUDTEL required?  

A: A 4-AUDTELS is required when you need a telephone riser, 1VRMS input or output audio riser, or have a 4-MIC or 4-FT installed on the 4-CPU’s user interface. A 4- ANNAUDTEL is required when you have a 4-MIC or 4-FT installed on the 4-ANNCPU’s user interface.  

Q: Does the 4-CU support Building Reports?  

A:  4-CU V4.02, while not specifically indicated, does support Building Reports by using the FireWorks export option.  

Q: What type of CPU is used in a graphic annunciator ?  

A: This will require use of the 4-CPUGRPH used in conjunction with 3-EVPWRA and 3- EVDVRA modules.  

Q: What hardware is required to support a PT-1S system printer?  

A: A printer can temporarily be used by plugging directly into a port on the 4-CPU however this will generate a ground fault.  For permanent installation a 4-USBHUB or 4- FWALx is required with Isolation Ports.  