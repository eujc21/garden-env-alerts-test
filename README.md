# Environment Alerts

### Overview
At Square Roots, we closely monitor the environment of each of our growing zones to ensure that our plants are growing in a consistent, optimal environment.
Every minute we collect air temperature, CO2 levels, relative humidity, water temperature, EC (Electrical Conductivity), and pH from our sensors and store them in our database for further analysis.

Most of the time these sensor values are within an acceptable range of values, but sometimes they're either too high or too low, which is usually indicative
of a problem with the system. We want to ensure that our farmers are alerted in real time when this happens.


### Challenge
Your challenge is to write an alerting system script that will evaluate whether or not each of these 6 parameters are within their acceptable ranges.
These ranges are:
* Air temperature range - 65.0-83.0°F
* Relative humidity range - 45.0-90.0%
* CO2 range - 800-1300ppm
* EC range - 1000-2500µs
* pH range - 5.7-7.0
* Water temperature range - 63.0-83.0°F

Your script should accept the path to a csv file as a command line argument. The csv (see [environemnt_data.csv](environment_data.csv)) will contain
columns for timestamp, as well as each of the 6 evironment parameters.

When an environment parameter goes out of range, print to STDOUT:

`MM/DD HH:MM - [COLUMN_NAME] has a value of [VALUE][UNITS] (expected [RANGE][UNITS])`

Example: `11/12 17:00 - air temperature has a value of 83.2°F (expected 65.0-83.0°F)`

When the parameter is back within it's range, print to STDOUT:

`MM/DD HH:MM - [COLUMN_NAME] is back within range of [RANGE][UNITS]`

Assumptions:

* CSV data is well formed (csv is valid, data types consistent, etc) and that the rows are in chronological order.
* Assume that everything is in range before the script is run.
* All ranges are inclusive, for instance 83.0°F is an acceptable air temperature value.
* You can treat all values as floats.
* Only print once when a parameter goes out of range (if it's out of range for minutes in a row, print one message)
* Only print once when a parameter is back in range
* Print all alerts for each minute at the same time (i.e. don't print all air temp alerts, then humidity, then CO2, etc.)
* Timestamps are in UTC and should be printed in 24hr UTC time
* You don't need to print units for pH (it's just a scale from 1-14)


### How to run (FILL IN HERE)
Include instructions below on how to run your script and any tests, including installing any required libraries. Please document any assumptions made as well.