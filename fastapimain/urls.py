from fastapi import APIRouter

from fastapimain import views

# The API model for one object.
from fastapimain.models import APISimulation

# The API model for a collection of objects.
from fastapimain.models import APISimulations

router = APIRouter()

router.get(
    "/simulation/",
    summary="Retrieve a list of all the simulations.",
    tags=["simulations"],
    response_model=APISimulations,
    name="simulations-get",
)(views.simulations_get)
router.post(
    "/simulation/",
    summary="Create a new simulation.",
    tags=["simulations"],
    response_model=APISimulation,
    name="simulations-post",
)(views.simulation_post)

router.get(
    "/simulation/{simulation_id}/",
    summary="Retrieve a specific simulation.",
    tags=["simulations"],
    response_model=APISimulation,
    name="simulation-get",
)(views.simulation_get)
router.put(
    "/simulation/{simulation_id}/",
    summary="Update a simulation.",
    tags=["simulations"],
    response_model=APISimulation,
    name="simulation-put",
)(views.simulation_put)
router.delete(
    "/simulation/{simulation_id}/",
    summary="Delete a simulation.",
    tags=["simulations"],
    response_model=APISimulation,
    name="simulation-delete",
)(views.simulation_delete)