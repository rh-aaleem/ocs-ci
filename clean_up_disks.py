from ocs_ci.framework import config as cluster_config

cluster_config.ENV_DATA["cluster_path"] = (
    "/Users/abdul/clusters/aaleem-bm0419/auth/kubeconfig"
)
cluster_config.RUN["kubeconfig"] = "/Users/abdul/clusters/aaleem-bm0419/auth/kubeconfig"

from ocs_ci.ocs.node import get_nodes
from ocs_ci.deployment.baremetal import clean_disks

workers = get_nodes(node_type="worker")
for worker in workers:
    clean_disks(worker)
