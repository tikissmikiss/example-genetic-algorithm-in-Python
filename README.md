#### README

This document provides information about the genetic algorithm implemented in the `ga.py` file. The algorithm aims to find a target password using different variants of the genetic algorithm.

#### Educational Implementation

Please note that this implementation is intended for educational purposes and may not be optimized for performance or production use.

#### Functionality

The genetic algorithm (GA) is an optimization technique based on biological evolution. In this project, the GA seeks to find a target password from an initial population of randomly generated individuals. Each individual represents a string of characters and evolves over generations to get closer to the target password. The fitness of an individual is determined by the number of characters that match the target password. The GA generates new generations by selecting the fittest individuals, applying genetic operators such as recombination and mutation, and evaluating their fitness until the target password is found or the maximum number of generations is reached.

#### Usage

2. Run the `ga.py` script with the desired arguments:

```bash
python ga.py <version> [-g MAX_GENERATIONS] [-p POPULATION_SIZE] [-e ELITE_RATE]
                     [-mR MUTATE_RATE] [-mP MUTATE_PROB] [-d DELAY] [-P PASSWORD]
                     [-v | -V] [-f | -F] [-s | -S] [-b | -B] [-Fs FITS_SIZE] [-Ss SOLUTIONS_SIZE]
```

   - `<version>`: Select the version of the algorithm you want to run. Options: 1, 2, 3, 4, 5, 6.

   Optional arguments:

   - `-g MAX_GENERATIONS`: Set the maximum number of generations (default: 50000).
   - `-p POPULATION_SIZE`: Set the population size (default: 100).
   - `-e ELITE_RATE`: Set the percentage of the population considered as elite (default: 0.2).
   - `-mR MUTATE_RATE`: Set the probability of an individual being selected for mutation (default: 0.1).
   - `-mP MUTATE_PROB`: Set the mutation probability of each gene of a selected individual (default: 0.2).
   - `-d DELAY`: Set the delay time between generations in milliseconds (default: 0).
   - `-P PASSWORD`: Set the target password that the algorithm should find (default: specified in the code).
   - `-v` or `--verbose=true`: Activate detailed information output (default: enabled).
   - `-V` or `--verbose=false`: Disable detailed information output (default: enabled).
   - `-f` or `--fitness=true`: Enable printing of all fitness values (default: enabled).
   - `-F` or `--fitness=false`: Disable printing of all fitness values (default: enabled).
   - `-s` or `--static=true`: Enable static output printing (default: enabled).
   - `-S` or `--static=false`: Disable static output printing (default: enabled).
   - `-b` or `--bests=true`: Enable printing of the best solutions (up to 40) (default: enabled).
   - `-B` or `--bests=false`: Disable printing of the best solutions (up to 40) (default: enabled).
   - `-Fs FITS_SIZE`: Set the number of fitness values to print (default: 40).
   - `-Ss SOLUTIONS_SIZE`: Set the number of solutions to print (default: 40).

3. The GA algorithm will run and display the results, including the version, statistics, and best solutions found.

---


#### README (en Español)

Este documento proporciona información sobre el algoritmo genético implementado en el archivo `ga.py`. El algoritmo tiene como objetivo encontrar una contraseña objetivo utilizando diferentes variantes del algoritmo genético.

#### Implementación Didáctica

Ten en cuenta que esta implementación está destinada con fines didácticos y puede que no esté optimizada para un rendimiento o uso en producción.

#### Funcionalidad

El algoritmo genético (AG) es una técnica de optimización basada en la evolución biológica. En este proyecto, el AG busca encontrar una contraseña objetivo a partir de una población inicial de individuos generados aleatoriamente. Cada individuo representa una cadena de caracteres y evoluciona a lo largo de las generaciones para acercarse a la contraseña objetivo. La aptitud de un individuo se determina por el número de caracteres que coinciden con la contraseña objetivo. El AG genera nuevas generaciones seleccionando los individuos más aptos, aplicando operadores genéticos como la recombinación y la mutación, y evaluando su aptitud hasta encontrar la contraseña objetivo o alcanzar el número máximo de generaciones.

#### Uso

2. Ejecuta el script `ga.py` con los argumentos deseados:

```bash
python ga.py <versión> [-g MAX_GENERATIONS] [-p POPULATION_SIZE] [-e ELITE_RATE]
                     [-mR MUTATE_RATE] [-mP MUTATE_PROB] [-d DELAY] [-P PASSWORD]
                     [-v | -V] [-f | -F] [-s | -S] [-b | -B] [-Fs FITS_SIZE] [-Ss SOLUTIONS_SIZE]
```

   - `<versión>`: Selecciona la versión del algoritmo que deseas ejecutar. Opciones: 1, 2, 3, 4, 5, 6.

   Argumentos opcionales:

   - `-g MAX_GENERATIONS`: Establece el número máximo de generaciones (valor por defecto: 50000).
   - `-p POPULATION_SIZE`: Establece el tamaño de la población (valor por defecto: 100).
   - `-e ELITE_RATE`: Establece el porcentaje de la población considerado como élite (valor por defecto: 0.2).
   - `-mR MUTATE_RATE`: Establece la probabilidad de que un individuo sea seleccionado para mutación (valor por defecto: 0.1).
   - `-mP MUTATE_PROB`: Establece la probabilidad de mutación de cada gen de un individuo seleccionado para mutación (valor por defecto: 0.2).
   - `-d DELAY`: Establece el tiempo de espera entre generaciones en milisegundos (valor por defecto: 0).
   - `-P PASSWORD`: Establece la contraseña objetivo que el algoritmo debe encontrar (valor por defecto: especificada en el código).
   - `-v` o `--verbose=true`: Activa la salida detallada de información (valor por defecto: activada).
   - `-V` o `--verbose=false`: Desactiva la salida detallada de información (valor por defecto: activada).
   - `-f` o `--fitness=true`: Habilita la impresión de todos los valores de aptitud (valor por defecto: habilitada).
   - `-F` o `--fitness=false`: Deshabilita la impresión de todos los valores de aptitud (valor por defecto: habilitada).
   - `-s` o `--static=true`: Habilita la impresión estática de salida (valor por defecto: habilitada).
   - `-S` o `--static=false`: Deshabilita la impresión estática de salida (valor por defecto: habilitada).
   - `-b` o `--bests=true`: Habilita la impresión de las mejores soluciones (hasta 40) (valor por defecto: habilitada).
   - `-B` o `--bests=false`: Deshabilita la impresión de las mejores soluciones (hasta 40) (valor por defecto: habilitada).
   - `-Fs FITS_SIZE`: Establece la cantidad de valores de aptitud a imprimir (valor por defecto: 40).
   - `-Ss SOLUTIONS_SIZE`: Establece la cantidad de soluciones a imprimir (valor por defecto: 40).

3. El algoritmo GA se ejecutará y mostrará los resultados, incluyendo la versión, estadísticas y mejores soluciones encontradas.

---

