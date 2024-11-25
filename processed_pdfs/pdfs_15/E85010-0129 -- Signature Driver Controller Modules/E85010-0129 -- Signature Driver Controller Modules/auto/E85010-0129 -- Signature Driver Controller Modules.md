# Signature Driver Controller Modules 3-SSDC1, 3-SDDC1, 3-SDC1  

# Overview  

The 3-SSDC1 and 3-SDDC1 Signature Driver Controller modules provide an intelligent interface between the 3-CPU3 module and Signature Series devices. Each module contains its own microprocessor used to coordinate, process and interpret information received from and sent to Signature devices. Power and communications is received directly from the control panel rail assembly. The 3-SSDC1 Single Signature Driver Controller module supports one Signature Data circuit, while the 3-SDDC1 Signature Dual Driver Controller module supports two Signature circuits. Both modules occupy one rail space in the fire alarm control cabinet and provide removable field wiring terminals to aid installation.  

Innovative design gives the 3-SSDC1/3-SDDC1 and Signature devices truly “distributed intelligence”. Signature detectors and modules have their own on-board microprocessor communicating with the loop controller in a fully digital communication format. This increases the accuracy of the information coming to and from the loop controller by reducing the effects of capacitance and noise.  

With decentralized intelligence much of the decision making moves from the loop controller to the devices. Advanced fire detection algorithms processed within the Signature devices effectively end unwanted alarms. Environmental compensation and multiple sensing element decision making operations are resident in the devices. Intelligent devices allow the Signature Controllers to execute communication and system functions with greater speed and low baud rates, increasing the accuracy of information transmitted between the loop controller and devices.  

# Standard Features  

•	 One or two circuit versions   
•	 Dedicated microprocessor control   
•	 Full digital communication Specialized communication protocol – Less sensitive to cable characteristics – Utilize existing wiring in most applications   
•	 Loop alarm in under 750 milliseconds Device location supervision – Unexpected additional device addresses – Missing device addresses – Switched device locations – Programmed device parameters   
•	 Automatic nonvolatile as-built mapping – Stores “actual” and “expected” device data – Stores physical connection sequence including “T” taps   
•	 Automatic day/night sensitivity Supports up to 250 intelligent Signature detectors and 250 Intelligent Signature Modules Up to five 3-SDDC1s per node – Total of 10 Signature circuits   
•	 Removable field wiring terminal blocks   
?Multiple survival modes — stand alone   
•	 Fully backward compatible with 3-SSDC and 3-SDDC Supports the full line of Signature II devices, including carbon monixide detection  

# Application  

Up to 125 detectors and 125 modules are supported over a single pair of wires by the 3-SDC1 Signature Cards that plug into the Signature controller modules. Loop distances over 11,000 feet (3300m) are possible. Class B wiring, Class A and Class X wiring are supported.  

The 3-SSDC1 and 3-SDDC1 use advanced communication formats that provide exceptional response. Using a “BROADCAST POLL” the loop controller checks the entire device circuit for any changes of state. Should one or more devices report a change the 3-SSDC1/3-SDDC1 uses “DIRECT ADDRESS SEARCH” to find reporting device(s). Devices that have entered the alarm state or become active are located nearly instantaneously.  

The unique use of “BROADCAST POLLING” combined with “DIRECT ADDRESS SEARCH” ensures that only new information is transmitted allowing a reduced baud rate with fast response time. The low baud rate is ideal for retrofit applications since in most applications existing wiring can be used.  

To enhance survivability of the system the 3-SSDC1/3-SDDC1 supports a standalone mode for Signature devices. Two catastrophic failure modes are supported. If the 3-CPU(1/3) fails, the loop controller will continue to poll its devices. If an alarm is detected it will be sent on the local rail communication bus and received by other local rail modules. A common alarm condition throughout the panel will result. If the local rail module (3-SSDC1/3-SDDC1) fails, and a device (smoke or module) detects an alarm, specialized circuitry will make the node aware of the alarm condition. The 3-CPU(1/3) will communicate the alarm condition to the rest of the network. Having multiple redundant modes is paramount in a life safety system.  

Every time the 3-SSDC1/3-SDDC1 communicates with a detector a green LED on the detector flashes. Normal green LED activity is not disturbing to building occupants, but can be quickly spotted by a maintenance technician. A red LED on the detector turns on only in the alarm condition.  

The 3-SSDC1/3-SDDC1 also supervises the device wiring, physical location of each device and the programmed device characteristics. This EDWARDS/Signature Series unique characteristic is accomplished by “MAPPING” the Signature circuit and committing the map to memory. Upon power up the loop controller will scan device serial numbers and map their physical location sequence on the loop, including “T” taps. After mapping is complete the controller automatically addresses each detector and module through downloading over the loop. There are no switches or dials to set. Each device is assigned a unique soft address generated by the site specific program.  

The 3-SSDC1/3-SDDC1 then compares the “Actual” physical device data to the “Expected” site specific program data. If any correlations are different, the loop controller issues a trouble to the CPU identifying the devices which do not match and posting a map fault. Through the 3-CPU3’s RS-232 port a graphical map of the loop can be uploaded depicting each device’s location on the loop, including branches (T-Taps) and all of the physical attributes associated with the device. This diagnostic information is unparalleled in the fire detection industry and vital for keeping accurate records on how the system was installed.  

During installation a common problem with analog/ addressable systems is locating ground faults. The 3-SSDC1 and 3-SDDC1 controllers have the ability to locate ground faults by specific module, speeding up the troubleshooting process. Another significant advantage of the 3-SSDC1/3-SDDC1 controllers during commissioning is electronic addressing and mapping. This eliminates duplicate addresses, which are also very difficult for most systems to locate.  

During maintenance, should groups of detector heads be removed for service and returned into the wrong smoke detector base (location), the 3-SSDC1/3-SDDC1 will automatically detect the problem. If the attributes of the switched devices are the same, the system will automatically download the correct soft addresses and algorithms to the devices (maintaining location supervision).  

If the attributes are not the same the 3-SSDC1/3-SDDC1 will send a map fault indication to the 3-CPU3 and post a trouble indicating the specific devices in fault.  

The 3-SSDC1/3-SDDC1 also monitors the Signature Series devices for maintenance and trouble conditions. Each smoke detector contains intelligence to adjust with environmental changes. This expands the amount of time required between cleaning while maintaining a constant alarm threshold. As the detector begins to exhaust the environmental compensation, and reaches the $80\%$ level, the 3-SSDC1/3-SDDC1 will indicate a maintenance alert or dirty condition to the 3-CPU and indicate the specific device requiring cleaning. If cleaning is not performed the detector will continue to operate until all of its environmental compensation is utilized. At this point the 3-SSDC1/3-SDDC1 sends a dirty trouble indication to the 3-CPU and posts a trouble condition. If maintenance is still not performed the Signature detector will automatically remove itself from service once the programmed threshold window has been breached (preventing a false alarm).  

When a detector includes carbon monoxide (CO) detection, the detector monitors its CO life remaining for the CO sensor element and provides this information automatically to the panel. For maintenance of the system the CO life remaining is also available by simply running a maintenance report at the panel or through the FireWorks graphical interface. A unique CO maintenance signal is automatically generated by the panel when there is $8\%$ (several months) of CO element life remaining. Should the CO sensor element not be replaced after the maintenance signal is reported, an “End of Life” trouble automatically posts on the panel when the CO sensor detection capability is exhausted.  

Remote test capability permits devices to be put in alarm, pre­ alarm, supervisory, monitor, or security alarm, or trouble from the panel menu or controls. This facilitates testing of smoke and heat detectors as well as monitor and security devices. Fast test is also provided for CO detectors allowing these devices to be tested quickly in the field.  

The 3-SSDC1 and 3-SDDC1 local rail modules modules are fully backwards compatible with the 3-SSDC and 3-SDDC local rail modules. 3-SSDC1 and 3-SDDC1 modules provide additional onboard memory to facilitate future Synergy functions. To upgrade a 3-SSDC/3-SDDC to a 3-SSDC1/3-SDDC1 respectively, replace the 3-SSDC/3-SDDC Local Rail Module with a 3-SDDC1-MB Local Rail Module and reuse the 3-SDC Signature Device Cards and filters.  

![](images/d357cb657f0abd0545ead320a516a609263900a8e614f4754bf2dde8f2144075.jpg)  
3-SSDC1, 3-DSDC1, and 3-SDDC1 Class B wiring  

3-SSDC1, 3-DSDC1, and 3-SDDC1 Class A and Class X wiring  

![](images/4ccb653cb40904077985dce347bb03ed3df37a688ab923b6f38f755b3e63f0b2.jpg)  

1. For Class A wiring, isolator modules and isolator detector bases are required to prevent wireto-wire shorts on the signaling line circuit wiring from adversely affecting other segments of the loop. Do not install more than 50 addressable devices between isolators, per NFPA 72.  

1 2. For Class X wiring, isolator modules and isolator detector bases are required to prevent wireto-wire shorts on the signaling line circuit wiring from adversely affecting any devices of the loop. 3. For Class X wiring, un-isolated devices must be mounted in a cabinet with isolators on the incoming and outgoing wiring.  

# Engineering Specification  

The communication format between the control panel and analog devices shall be $100\%$ digital.  

Loop alarm recognition must be within 750 milliseconds of a device going into the alarm state, with system response time no greater than 3 seconds. All devices shall support remote testing. It must be possible to wire the circuit as Class B, Class A or Class X with non-shielded, non-twisted wire. It must be possible to wire branches (T-taps) with Class B wiring.  

The driver controller must be manufactured in accordance with ISO 9001 standards.  

The system must have tolerance to multiple failures. There must be a standalone mode of operation that will ensure the system is aware of alarms even if the local rail or main CPU fails.  

# Specifications (Signature Circuits)  

Charts assume wire and devices are evenly distributed over length of circuit  

Non-twisted, non shielded wire   


<html><body><table><tr><td>Device type</td><td>#ofDetectors</td><td>#ofModule Addresses</td><td>#14AWG(20pf/foot) (2.53Ohm/1000ft)</td><td>#16AWG(20pf/foot) (4.020hm/1000ft)</td><td>#18AWG(20pf/foot) (6.380hm/1000ft)</td></tr><tr><td>Detectorsonly</td><td>125</td><td>0</td><td>14,752 feet (4,497 meters)</td><td>9,275 feet (2,827 meters)</td><td>5,839feet (1,780 meters)</td></tr><tr><td>Modulesonly</td><td>0</td><td>125</td><td>12,599 feet(3,840 meters)</td><td>7,921 feet (2,414 meters)</td><td>4,986 feet (1,520 meters)</td></tr><tr><td>DetectorsandModules</td><td>125</td><td>125</td><td>5,738feet (1,749 meters)</td><td>3,608feet (1,100 meters)</td><td>2,271feet (692 meters)</td></tr><tr><td>DetectorsandModules with2-wiresmokes</td><td>63</td><td>55+9SIGA-UM</td><td>7,623feet (2,324 meters)</td><td>4,793 feet (1,461 meters)</td><td>3,017feet (920meters)</td></tr><tr><td>Modules with2-wiresmokes</td><td>0</td><td>107+9SIGA-UM</td><td>3,798feet (1,158 meters)</td><td>2,388feet (728 meters)</td><td>1,503feet (458 meters)</td></tr></table></body></html>  

Twisted pair non shielded wire   


<html><body><table><tr><td rowspan="2">Device Type</td><td rowspan="2">#ofDetectors</td><td rowspan="2">#ofModule Addresses</td><td rowspan="2">#14AWG (38pf/foot) (2.53 Ohm/1000ft)</td><td rowspan="2">1.5mm2 (36pf/foot) (3.75 Ohm/1000ft)</td><td rowspan="2">#16AWG (36pf/foot) Ohm/1000ft)</td><td rowspan="2">1.0mm2 (25pf/foot) (5.51 Ohm/1000ft)</td><td rowspan="2">#18AWG (25pf/foot) (6.38 Ohm/1000ft)</td></tr><tr><td>(4.02</td></tr><tr><td>Detectorsonly</td><td>125</td><td>0</td><td>13,157feet (4,010 m)</td><td>9,933feet (3,028 m)</td><td>9,275feet (2,827 m)</td><td>6,760feet (2,061 m)</td><td>5,839feet (1,780 m)</td></tr><tr><td>Modules Only</td><td>0</td><td>125</td><td>12,599feet (3,840 m)</td><td>8,483 feet (2,586 m)</td><td>7,921 feet (2,414 m)</td><td>5,774 feet (1,760 m)</td><td>4,986feet (1,520 m)</td></tr><tr><td>Detectors &Modules Detectorsand</td><td>125</td><td>125</td><td>5,738feet (1,749 m)</td><td>3,864 feet (1,178 m)</td><td>3,608 feet (1,100 m)</td><td>2,630 feet (802 m)</td><td>2,271 feet (692 m)</td></tr><tr><td>modules with 2-wiresmokes</td><td>63</td><td>55+9SIGA-UM</td><td>7,623feet (2,324 m)</td><td>5,133feet (1,565 m)</td><td>4,793 feet (1,461 m)</td><td>3,494feet (1,065 m)</td><td>3,017feet (920 m)</td></tr><tr><td>Moduleswith 2-wiresmokes</td><td>0</td><td>107+9SIGA- UM</td><td>3,798feet (1,158 m)</td><td>2,558feet (780 m)</td><td>2,388feet (728 m)</td><td>1,741 feet (531 m)</td><td>1,503feet (458 m)</td></tr></table></body></html>  

Twisted pair shielded wire   


<html><body><table><tr><td>DeviceType</td><td>#ofDetectors</td><td>#ofModule Addresses</td><td>#14AWG(84pf/foot) (2.530hm/1,000ft)</td><td>#16AWG（82pf/foot) (4.020hm/1,000ft)</td><td>#18AWG（58pf/foot) (6.380hm/1,000ft)</td></tr><tr><td>Detectorsonly</td><td>125</td><td>0</td><td>5,952feet (1,814 meters)</td><td>6,098 feet (1,859 meters)</td><td>5,839feet (1,780 meters)</td></tr><tr><td>ModulesOnly</td><td>0</td><td>125</td><td>5,952feet (1,814 meters)</td><td>6,098 feet (1,859 meters)</td><td>4,986 feet (1,520 meters)</td></tr><tr><td>Detectors&Modules</td><td>125</td><td>125</td><td>5,738feet (1,749 meters)</td><td>3,608feet (1,100meters)</td><td>2,271feet (692 meters)</td></tr><tr><td>Detectorsandmodules with2-wiresmokes</td><td>63</td><td>55+9SIGA-UM</td><td>5,952feet (1,814 meters)</td><td>4,793feet (1,461 meters)</td><td>3,017feet (920meters)</td></tr><tr><td>Moduleswith2-wire smokes</td><td>0</td><td>107+9SIGA-UM</td><td>2,558feet (780 meters)</td><td>2,388feet (728 meters)</td><td>1,503feet (458 meters)</td></tr></table></body></html>  

<html><body><table><tr><td>Catalog Number</td><td>3-SSDC1</td><td>3-SDDC1</td></tr><tr><td>Installation</td><td>1 LRM Space</td><td>1 LRM Space</td></tr><tr><td>Module Configuration</td><td>1 Addressable circuit (3-SDC1 Card) expandable to 2 circuits.</td><td>2 Addressable circuits (3-SDC1 Cards)</td></tr><tr><td>Operating Current [Note 2]</td><td>Standby 144 mA Alarm 204 mA</td><td>Standby 264 mA Alarm 336 mA</td></tr><tr><td>Operating Voltage</td><td colspan="2">24 Vdc, Nominal</td></tr><tr><td>AddressRequirements</td><td colspan="2">Automatic</td></tr><tr><td>Detectors Supported</td><td colspan="2">125 per 3-SDC1 Card</td></tr><tr><td>Modules Supported</td><td colspan="2">125 Module Addresses per 3-SDC1 Card</td></tr><tr><td>2-Wire Smoke Power Output</td><td colspan="2">100 mA per 3-SDC1 Card (not included in Operating Current above</td></tr><tr><td>Conventional detectorssupported</td><td colspan="2">150 of 100 μA type per circuit.</td></tr><tr><td>Signature Circuit Voltage</td><td colspan="2">20 VDC+/-5%</td></tr><tr><td>Maximum Signature Circuit Resistance</td><td colspan="2">100 Ohms</td></tr><tr><td>Maximum Signature Circuit Capacitance</td><td colspan="2">0.33 μF</td></tr><tr><td>Communications Format</td><td colspan="2">100% Digital</td></tr><tr><td>Circuit Wiring Styles</td><td colspan="2">Class B, Class A or Class X</td></tr><tr><td>Termination</td><td colspan="2">Removable plug-in terminal strip(s) on module</td></tr><tr><td>Permissable Wire Size</td><td colspan="2">18 to 12 AWG (0.75 to 2.5 mm2)</td></tr><tr><td>Agency Listings</td><td colspan="2"></td></tr><tr><td>Operating Environment Note 1: Other EST3 components are modularly listed under the following standards:</td><td colspan="2">UL,ULC (see Note 1);CE,LPCB,EN54 (see Note 3) 32 °F (0 °C) to 120 °F (49 °C) 93% RH, non-condensing</td></tr><tr><td colspan="3">UL 864 categories: UOJZ, UOXX, UUKL and SYZV, UL 294 category ALVY, UL 609 category AOTX, UL 636 category ANET, UL 1076 category APOU, UL 365 category APAW, UL 1610 category AMCX, UL 1635 category AMCX ULC-S527,ULC-S301,ULC-S302,ULC-S303,ULC-S306,ULC/ORD-C1076,ULC/ORD-C693</td></tr><tr><td colspan="3">PleaserefertoEST3InstallationandServiceManualforcompletesystemrequirements. Note 2: Current shown Includes fulloop of devices. loop controller compatibility).</td></tr></table></body></html>  

# Ordering Information  

<html><body><table><tr><td>Catalog Number</td><td>Description</td><td>Shipping Wt. Ib (kg)</td></tr><tr><td>3-SSDC1</td><td>SingleSignatureDriverController.Comeswithone3-SDC1DeviceCard.MountstoLocalRail.Add suffix“-E"for EN54compliantversions.</td><td>0.5 (0.23)</td></tr><tr><td>3-SDDC1</td><td>DualSignatureDriverController.Comeswithtwo3-SDC1s. MountstoLocalRail.Addsuffix“-E"forEN54compliantversions</td><td>0.5 (0.23)</td></tr><tr><td>3-SDC1</td><td>Signature Device Card - upgrades a 3-SSDC1 to a 3-SDDC1. Addsuffix“-E"forEN54compliantversions.</td><td>0.25 (0.11)</td></tr><tr><td>3-FP</td><td>FillerPlate,orderseparatelywhennoLEDorLED/Switchmoduleinstalled.</td><td>0.1 (0.05)</td></tr></table></body></html>  