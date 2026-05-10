from src.data.make_interim import run_make_interim
from src.features.build_features import run_build_features
from src.models.train import run_train_model
from src.models.evaluate import run_evaluate


def run_pipeline():
    print("1. Gerando dataset interim...")
    run_make_interim()

    print("2. Construindo features...")
    run_build_features()
#
    print("3. Treinando modelo...")
    run_train_model()
#
    print("4. Avaliando modelo...")
    run_evaluate()

    print("Pipeline finalizado!")


if __name__ == "__main__":
    run_pipeline()