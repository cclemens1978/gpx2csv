# gpx2csv

*gpx2csv*: This script converts the waypoints from a GPX file into an alphabetically sorted CSV file. In particular, I wrote this script to convert the file *favourites.gpx*, which is created by the navigational software *OsmAnd+* on *Android*, into an easier to read format. *OsmAnd+* saves the waypoints unsorted in an XML based file format. In contrast, I prefer a simple text file in CSV format, which contains only one waypoint per line including its category, name and coordinates. This increases the clarity, and the alphabetical sorting makes it possible to compare two files.

## Installation

``` bash
sudo aptitude install git
git clone https://github.com/cclemens1978/gpx2csv.git

sudo aptitude install python3 python3-pip

sudo pip3 install xmltodict
```

## Usage

``` bash
python gpx2csv.py favourites.gpx
```

Almost immediately, the newly created file *waypoints_YYYYMMDD_HHMMSS.csv* containing the alphabetically sorted waypoints appears in the current directory. Here, the time information in the file name and the timestamp of the output file corresponds to the timestamp of the input file.

## Support and Team

Send your suggestions and bug reports to Christian Clemens <<christian.clemens@web.de>>.

## Acknowledgements

This script makes use of software developed by Martin Blech ([xmltodict](https://pypi.org/project/xmltodict/)).

## License

tbd
