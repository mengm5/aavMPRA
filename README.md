# aavMPRA
aavMPRA is a simple tool to obtain readCounts of the candidate enhancers generated from our AAV-MPRA library.
#### Tutorial: https://github.com/mengm5/aavMPRA/blob/main/Tutorial_of_aavMPRA.pdf
***
## Intallation
* ### Clone the repository:
  ​```
  git clone https://github.com/mengm5/aavMPRA.git
​  ```
* ### Enter the aavMPRA directory:
  ```
  cd /your_path_to_aavMPRA/aavMPRA
  ls
  # aavMPRA  aavMPRA_environment.yml  data  file_description.txt  index  src  test
  export PATH=/your_path/aavMPRA/aavMPRA:$PATH
  ```
* ### Install dependencies via conda
  * #### Install conda if it is not on your server (https://docs.conda.io/en/latest/miniconda.html).
  * #### Once conda is installed, create aavMPRA environment by the following command: 
    ```
    conda env create -n aavMPRA -f aavMPRA_environment.yml
    ```

* ### Install dependencies via packages
  * #### If you don't use conda to install dependencies, you can install them locally.
  * #### Dependencies: 
    ```
    python=3.12.2 (https://www.python.org/)
    pip:
      - altgraph==0.17.4
      - numpy==2.0.0
      - packaging==24.1
      - pandas==2.2.2
      - pyinstaller==6.8.0
      - pyinstaller-hooks-contrib==2024.7
      - python-dateutil==2.9.0.post0
      - pytz==2024.1
      - six==1.16.0
      - tzdata==2024.1
    bowtie=1.3.1 (https://bowtie-bio.sourceforge.net/index.shtml)
    bowtie2=2.5.4 (https://bowtie-bio.sourceforge.net/bowtie2/index.shtml)
    samtools=1.20 (https://www.htslib.org/)
    ```
***
## Usage
* ### Build the bowtie/bowtie2 index by the following command if it is not been built:
  ```
  bowtie-build ref.fa /your_path_to_save_index/index_name
  bowtie2-build ref.fa /your_path_to_save_index/index_name

  # Please refer to the tutorial for details on how to construct ref.fa.
  # The pre-build index is at /your_path/aavMPRA/index for testing.
  ```
  
* ### Create a fastq_info.txt file. This file contains 4 columns:
  * #### 1) the first column is paths where fastqs exist, 
  * #### 2) the second is the original names of fastqs, 
  * #### 3) the third is names that you want to change, 
  * #### 4) the forth is used to distinguish read1 (R1) and read2 (R2).
  ```
  # The example file is at /your_path/aavMPRA/data.

  vim /your_path/aavMPRA/data/fastq_info.txt

  #
  Path	Fastq	Rename	Read
  /aavMPRA/data	test1_1.fastq.gz	Test1	R1
  /aavMPRA/data	test1_2.fastq.gz	Test1	R2
  /aavMPRA/data	test2_1.fastq.gz	Test2	R1
  /aavMPRA/data	test2_1.fastq.gz	Test2	R2
  ```
  
* ### Create a parameter.txt file. This file contains 6 columns:
  * #### 1) the first column is names of steps,
  * #### 2) the second is names of parameters,
  * #### 3) the third is the assignment of parameters,
  * #### 4) the forth is the description of parameters,
  * #### 5) the fifth is the tools to which the parameters belong,
  * #### 6) the sixth is the execution mode, the mutagenesis mode uses bowtie to map reads and the common mode uses bowtie2. 
  ```
  # The example file is at /your_path/aavMPRA/data.

  vim /your_path/aavMPRA/data/parameter.txt

  #
  Steps	Name	Parameter	Explanation	Tool	Mode
  rmAdapters	"-g"	GCAGATGGCTCTTTGTCCTA	"5' adapter to be removed from R1"	cutadapt	generic
  rmAdapters	"-G"	AAGTATCTTTCCTGTGCCCA	"5' adapter to be removed from R2"	cutadapt	generic
  ```

* ### After preparing all input files, run the pipeline by the following command:
  ```
  aavMPRA -o /output_path \ 
  -f /path_to_fastq_info/fastq_info.txt \
  -p /path_to_parameter/parameter.txt \
  -m [mutagenesis/common] \ 
  -i /path_to_index/index_name \
  [--gz]

  # output_path: absolute path is recommended.
  # -m input mutagenesis or common.
  # if the fastq file saved as .gz file, please add --gz.
  ```

* ### The aavMPRA will generate .sh file sequentially to execute analysis:
  * #### 1) 0_softlink.sh: read the fastq_info.txt and generate a file path that contains softlinks of fastqs with standard names.
  * #### 2) 1.1_rmAdapters.sh, 1.2_getUMIs.sh, 1.3_rmUMIs.sh: correct reads structure by cutadapt.
  * #### 3) 2_mapReads.sh: map reads to the bowtie/bowtie2 index.
  * #### 4) 3.1_extractReadnames.sh, 3.2_extractUMIs.sh: extract readnames from .sam file and UMIs from fastqs.
  * #### 5) 3.3_matchPairs.sh: combine readnames and UMIs.
  * #### 6) 3.4_countUMIs.sh, 3.5_mergeSamples.sh: generate readcounts file and merge all readcounts of samples into one.

If you want to reanalyze from the middle of all steps and do not want to start from the beginning, it is recommended to modify these .sh files.
