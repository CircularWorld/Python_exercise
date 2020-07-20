
class SkillManager:
    def skillmanager(self):
        print("调用SkillManager")
# 3. 在skill_manager.py中调用skill_deployer.py中实例方法。

from common.skill_system.skill_deployer import SkillDeployer

sd = SkillDeployer()
sd.skilldeployer()