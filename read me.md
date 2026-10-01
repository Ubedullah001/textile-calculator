# 🧵 Textile Fabric Production Rate Calculator

A Streamlit web application designed to calculate the production rate of fabric in the textile industry.

This application helps users calculate estimated fabric production based on machine speed, fabric width, machine efficiency, operating hours, number of machines, and fabric GSM.

## 🚀 Features

- Calculate production per minute
- Calculate production per hour
- Calculate production per day
- Calculate production for multiple machines
- Calculate fabric weight in kg
- Calculate production using machine efficiency
- Simple and user-friendly interface
- Interactive Streamlit dashboard

## 📁 Project Structure

```text
textile-fabric-production-calculator/
│
├── app.py
├── requirements.txt
└── README.md

📊 Input Parameters

The application requires the following information:

Machine Type

Machine Speed

Fabric Width

Machine Efficiency

Operating Hours per Day

Fabric GSM

Number of Machines

🧮 Calculation Formulas
Effective Speed
Effective Speed = Machine Speed × Efficiency / 100

Production per Hour
Production per Hour = Effective Speed × 60

Production per Day
Production per Day =
Production per Hour × Operating Hours × Number of Machines

Fabric Weight
Fabric Weight (kg) =
Length × Width × GSM / 1000

⚙️ Installation

Clone the repository from GitHub:

git clone https://github.com/YOUR-USERNAME/textile-fabric-production-calculator.git


Open the project folder:

cd textile-fabric-production-calculator


Create a virtual environment:

python -m venv venv


Activate the virtual environment on Windows:

venv\Scripts\activate


Install the required packages:

pip install -r requirements.txt

▶️ Run the Application

Run the following command:

streamlit run app.py


After running the command, the application will open in your web browser.

📈 Example

Example input values:

Machine Speed: 500
Fabric Width: 1.60 meters
Machine Efficiency: 85%
Operating Hours: 24
Fabric GSM: 150
Number of Machines: 1


The application will calculate:

Production per Minute
Production per Hour
Production per Day
Fabric Weight per Day

⚠️ Important Note

The current version uses a general production-rate calculation.

For actual textile weaving production, additional parameters may be required, including:

Loom RPM

Picks per minute

Picks per inch (PPI)

Picks per centimeter (PPC)

Loom efficiency

Reed width

Fabric take-up

Warp specification

Weft specification

For knitting machines, additional parameters may include:

Machine RPM

Machine diameter

Number of feeders

Gauge

Loop length

Machine efficiency

The calculation formulas should be adjusted according to the specific textile machine and production process.

🔮 Future Improvements

The application can be expanded with:

Weaving production calculator

Knitting production calculator

Yarn consumption calculator

GSM calculator

Fabric consumption calculator

Loom efficiency calculator

Production target calculator

Shift-wise production reports

Daily production charts

Monthly production charts

Excel export

PDF production reports

Production history

Database integration

Production KPI dashboard

🛠️ Technologies Used

Python

Streamlit

Pandas

NumPy

📄 License

This project is intended for educational, research, and textile production calculation purposes.

👨‍💻 Project

Textile Fabric Production Rate Calculator

A web-based tool for calculating and analyzing fabric production rates in textile manufacturing.

:::

Is file ko GitHub mein **`README.md`** ke naam se save karein.
