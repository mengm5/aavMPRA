# aavMPRA
aavMPRA is a simple tool to obtain readCounts of the candidate enhancers generated from our AAV-MPRA library.
#### Tutorial: https://github.com/mengm5/aavMPRA/blob/main/Tutorial%20of%20aavMPRA.pdf
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
  # aavMPRA  aavMPRA_environment.yml  data  index  src  test  Tutorial_of_aavMPRA.pdf
  ```
* ### Install dependencies via conda
  * #### Install conda if it is not on your server (https://docs.conda.io/en/latest/miniconda.html).
  * #### Once conda is installed, create aavMPRA environment by the following command: 
    ```
    conda env create -n aavMPRA -f aavMPRA_environment.yml
    ```

* ### Install dependencies via packages
  * #### If you cannot use conda to install dependencies, you can install them locally.
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
    ```
