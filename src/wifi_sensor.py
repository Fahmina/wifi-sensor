import asyncio
from typing import Any, ClassVar, Dict, Mapping, Optional
from viam.components.sensor import Sensor
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase
from viam.resource.types import Model, ModelFamily

class MySensor(Sensor):
    # Subclass the Viam Sensor component and implement the required functions
    MODEL: ClassVar[Model] = Model(ModelFamily("viam", "wifi_sensor"), "linux")

    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        sensor = cls(config.name)
        return sensor

    async def get_readings(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> Mapping[str, Any]:
        with open("/proc/net/wireless") as wifi_stats:
            content = wifi_stats.readlines()
            quality = content[2]
            quality = quality.split(" ")
            clean_quality = [x for x in quality if x != '']
            return {"wifi-link": clean_quality[2], "wifi-level": clean_quality[3], "wifi-noise": clean_quality[4]}

async def main():
    wifi=MySensor(name="wifi")
    signal = await wifi.get_readings()
    print(signal)

if __name__ == '__main__':
    asyncio.run(main())
