import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class DataPrepare:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.file_path)
        return self.df

    def preprocess(self):
        self.df[['Min Salary', 'Max Salary']] = self.df['Salary Range'].str.split('-', expand=True)

        self.df['Min Salary'] = self.df['Min Salary'].str.replace('[£,]', '', regex=True).str.strip()
        self.df['Max Salary'] = self.df['Max Salary'].str.replace('[£,]', '', regex=True).str.strip()

        self.df['Min Salary'] = self.df['Min Salary'].astype(float)
        self.df['Max Salary'] = self.df['Max Salary'].astype(float)

        self.df['Average Salary'] = (self.df['Min Salary'] + self.df['Max Salary']) / 2

        self.df['Year'] = pd.to_datetime(self.df['Date Posted']).dt.year

        return self.df


class BarPlot:
    def __init__(self, df):
        self.df = df

    def plot(self):
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Experience Level', y='Average Salary', data=self.df)
        plt.title('Середня зарплата за рівнем досвіду')
        plt.xticks(rotation=45)
        plt.show()


class BoxPlot:
    def __init__(self, df):
        self.df = df

    def plot(self):
        plt.figure(figsize=(12, 6))
        sns.boxplot(x='Industry', y='Average Salary', data=self.df)
        plt.title('Розподіл зарплат за галузями')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()


class HeatMap:
    def __init__(self, df):
        self.df = df

    def plot(self):
        pivot_table = pd.crosstab(self.df['Experience Level'], self.df['Industry'])

        plt.figure(figsize=(10, 6))
        sns.heatmap(pivot_table, annot=True, cmap='viridis')
        plt.title('Кількість вакансій за досвідом і галуззю')
        plt.show()


class ScatterPlot:
    def __init__(self, df):
        self.df = df

    def plot(self):
        plt.figure(figsize=(10, 6))
        sns.scatterplot(
            x='Year',
            y='Average Salary',
            hue='Experience Level',
            data=self.df
        )
        plt.title('Залежність зарплати від року')
        plt.show()


class PairPlot:
    def __init__(self, df):
        self.df = df

    def plot(self):
        sns.pairplot(self.df[['Average Salary', 'Year']], diag_kind='kde')
        plt.show()


def main():
    loader = DataPrepare('Job opportunities.csv')

    df = loader.load_data()
    df = loader.preprocess()

    BarPlot(df).plot()
    BoxPlot(df).plot()
    HeatMap(df).plot()
    ScatterPlot(df).plot()
    PairPlot(df).plot()

if __name__ == "__main__":
    main()