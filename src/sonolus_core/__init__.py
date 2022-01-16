from pathlib import Path

from single_source import get_version

from .database import (
    BackgroundInfo,
    Database,
    EffectInfo,
    EngineInfo,
    InfoBase,
    InfoDetails,
    InfoList,
    LevelInfo,
    LocalizationText,
    ParticleInfo,
    SkinInfo,
    localize,
)
from .exceptions import ParseVersionException
from .resource import compress, hash
from .typings import (
    SRL,
    BackgroundConfiguration,
    BackgroundData,
    BackgroundItem,
    EffectClip,
    EffectData,
    EffectDataClip,
    EngineConfiguration,
    EngineConfigurationAnimation,
    EngineConfigurationAnimationTween,
    EngineConfigurationJudgmentErrorPlacement,
    EngineConfigurationJudgmentErrorStyle,
    EngineConfigurationMetric,
    EngineConfigurationOption,
    EngineConfigurationSliderOption,
    EngineConfigurationToggleOption,
    EngineConfigurationUI,
    EngineConfigurationVisibility,
    EngineData,
    EngineDataArchetype,
    EngineDataArchetypeData,
    EngineDataBucket,
    EngineDataFunctionName,
    EngineDataFunctionNode,
    EngineDataNode,
    EngineDataScript,
    EngineDataScriptCallback,
    EngineDataSprite,
    EngineDataValueNode,
    EngineItem,
    Fit,
    ItemBase,
    ItemDetails,
    ItemList,
    LevelData,
    LevelDataEntity,
    LevelDataEntityData,
    LevelItem,
    OptionName,
    ParticleData,
    ParticleDataEffect,
    ParticleDataGroup,
    ParticleDataGroupParticle,
    ParticleDataGroupParticlePropertyExpression,
    ParticleDataSprite,
    ParticleEffect,
    ParticleItem,
    ResourceTypeLiteral,
    ServerInfo,
    SkinData,
    SkinDataExpression,
    SkinDataSprite,
    SkinDataTransform,
    SkinItem,
    SkinSprite,
    UseItem,
    customEffectClip,
    customParticleEffect,
    customSkinSprite,
    easeTypes,
)
from .version import Version, current_version, get_latest_version

__version__ = get_version(__name__, Path(__file__).parent.parent.parent)

__all__ = [
    "ParseVersionException",
    "compress",
    "hash",
    "Version",
    "current_version",
    "get_latest_version",
    "BackgroundInfo",
    "Database",
    "EffectInfo",
    "EngineInfo",
    "InfoBase",
    "InfoDetails",
    "InfoList",
    "LevelInfo",
    "localize",
    "LocalizationText",
    "ParticleInfo",
    "SkinInfo",
    "BackgroundData",
    "BackgroundConfiguration",
    "BackgroundItem",
    "EffectData",
    "EffectDataClip",
    "EffectClip",
    "customEffectClip",
    "EngineConfiguration",
    "EngineConfigurationOption",
    "EngineConfigurationSliderOption",
    "EngineConfigurationToggleOption",
    "EngineConfigurationUI",
    "EngineConfigurationJudgmentErrorPlacement",
    "EngineConfigurationJudgmentErrorStyle",
    "EngineConfigurationAnimation",
    "EngineConfigurationVisibility",
    "EngineConfigurationMetric",
    "EngineConfigurationAnimationTween",
    "OptionName",
    "EngineData",
    "EngineDataSprite",
    "EngineDataFunctionName",
    "EngineDataBucket",
    "EngineDataArchetypeData",
    "EngineDataArchetype",
    "EngineDataScriptCallback",
    "EngineDataScript",
    "EngineDataValueNode",
    "EngineDataFunctionNode",
    "EngineDataNode",
    "EngineItem",
    "Fit",
    "ItemBase",
    "ResourceTypeLiteral",
    "ItemDetails",
    "ItemList",
    "LevelData",
    "LevelDataEntity",
    "LevelDataEntityData",
    "LevelItem",
    "UseItem",
    "ParticleItem",
    "ParticleData",
    "ParticleEffect",
    "customParticleEffect",
    "ParticleDataGroupParticlePropertyExpression",
    "easeTypes",
    "ParticleDataGroupParticle",
    "ParticleDataGroup",
    "ParticleDataSprite",
    "ParticleDataEffect",
    "ServerInfo",
    "SkinData",
    "SkinDataSprite",
    "SkinDataTransform",
    "SkinDataExpression",
    "SkinItem",
    "customSkinSprite",
    "SkinSprite",
    "SRL",
]
