# Polymer Entanglement Analysis

## Table of Contents

- [Using the Z1+ Package for Polymer Entanglement Analysis](#using-the-z1-package-for-polymer-entanglement-analysis)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Installation Steps](#installation-steps)
  - [Additional Tips for Northwestern Students with QUEST access](#additional-tips-for-northwestern-university-students-with-quest-access)
- [Usage](#usage)
- [Performing Primitive Path Analysis (PPA)](#performing-primitive-path-analysis-ppa)
- [Visualization in OVITO](#visualization-in-ovito)
- [Example](#example)
- [License](#license)

---

## Using the Z1+ Package for Polymer Entanglement Analysis

This repository provides guidance on using the **Z1+ package** for analyzing polymer entanglements. The Z1+ tool enables detailed analysis of entanglements within polymer networks.

### Step 1: Access the Z1+ Package

First, visit the official Mendeley page to download the Z1+ package:

[Z1+ Package - Mendeley Data](https://data.mendeley.com/datasets/m425t6xtwr/1)

This package accompanies the work titled *"The Z1+ package: Shortest multiple disconnected path for the analysis of entanglements in macromolecular systems."* Be sure to thoroughly read the accompanying paper before using the tool.

---

## Installation

### Prerequisites

Ensure the following software is installed:

- [Perl](https://www.perl.org/get.html)
- [Python](https://www.python.org/)

Installation of these dependencies is not covered in this guide.

### Installation Steps

1. **Download the Z1+ Package**

   Download the `Z1+.tar.gz` file from the [Mendeley page](https://data.mendeley.com/datasets/m425t6xtwr/1) into a local directory, for example, `Z1_plus_setup`.

2. **Extract the Package**

   Open your terminal, navigate to the `Z1_plus_setup` directory, and extract the contents of the package:

   ```bash
   tar -xvzf Z1+.tar.gz
   ```

### Step 3: Install the Z1+ Package

To install the Z1+ package, execute the following command in your terminal:

```bash
perl Z1+install.pl
```


4. **Move the Z1+ Binary to a Preferred Location**

   To avoid running Z1+ from its installation directory, you should copy the Z1+ binary to a more convenient location. Run the following commands in your terminal:

   ```bash
   mkdir ../Z1_plus
   cp Z1+ ../Z1_plus/Z1+
   ```

Installation is now complete.



### Additional Tips (for Northwestern University Students with QUEST Access)

If you have access to QUEST, follow these specific instructions to set up Z1+:

1. Install Z1+ in your home directory for proper access.
2. Load a compatible version of Perl before proceeding with the installation by running the following command:

   ```bash
   module load perl/5.26
   ```

This ensures that the correct Perl version is available on QUEST before you install Z1+.


## Usage

To use the Z1+ package for entanglement analysis, refer to the **"User Manual"** section in the paper:

> *"The Z1+ package: Shortest multiple disconnected path for the analysis of entanglements in macromolecular systems."*

This section provides detailed instructions on configuring the tool and running various analyses.

---

## Performing Primitive Path Analysis (PPA)

To perform a **Primitive Path Analysis (PPA)** using Z1+, run the following command in your terminal:

```bash
<path_to_Z1+>/Z1+ -p <configuration-file>
```

Replace <path_to_Z1+> with the actual path where you copied the Z1+ executable, and <configuration-file> with the configuration file for your system. For more details on configuring this analysis, refer to the documentation provided in the main Z1+ paper.


## Visualization in OVITO

To visualize the primitive paths generated by the Z1+ PPA:

1. Copy the Python script `translate.py` to the directory where the `PPA+.dat` file (outputted by Z1+) is located.
2. Convert the `.dat` file into an easy-to-read XYZ format by running the following command:

   ```bash
   python translate.py
   ```

3. The script will generate a file named reformatted_data.txt.
4. Open OVITO, then drag and drop reformatted_data.txt into the open OVITO window.
5. When prompted, complete the column mapping:
  Column 1: Particle Type
  Column 2: Position X
  Column 3: Position Y
  Column 4: Position Z

Click OK to finish, and the visualization should now appear in OVITO.

## Example

Below is an example of a `reformatted_data.txt` file generated from a polymer melt analyzed using the Z1+ PPA. Please note that:

- The coordinates in the file are **unwrapped**, meaning they may extend beyond the original simulation box.
- The **simulation cell boundaries** are not preserved in this output, as the focus is on the primitive paths.

![Example Image](images/example.png)

---

## License

This project is licensed under the MIT License. For more information, refer to the [LICENSE](LICENSE) file.


