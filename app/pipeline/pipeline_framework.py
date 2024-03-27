import sys
from step_factory import StepFactory
import yaml


# ステップクラスのインポート
from download_step import DownloadStep
from data_extraction_step import DataExtractionStep
from attribution_processing_step import AttributionProcStep
from web_scraper_step import WebScraperStep
from service_catalog_creator_step import ServiceCatalogCreatorStep

# ステップをファクトリーに登録
StepFactory.register_step('download', DownloadStep)
StepFactory.register_step('data_extraction', DataExtractionStep)
StepFactory.register_step('attribution_proc', AttributionProcStep)
StepFactory.register_step('web_scraper_step', WebScraperStep)
StepFactory.register_step('service_catalog_creator_step', ServiceCatalogCreatorStep)

def execute_pipeline(pipeline_config_path):
    with open(pipeline_config_path, 'r') as file:
        pipeline_config = yaml.safe_load(file)

    for step_config in pipeline_config.get('steps', []):
        # skip_flgがtrueとして評価されるかどうかをチェック
        if step_config.get('skip_flg', False) == True:
            print(f"Skipping step: {step_config['name']}")
            continue

        step = StepFactory.create_step(step_config['type'], step_config)
        step.execute()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        execute_pipeline(sys.argv[1])

