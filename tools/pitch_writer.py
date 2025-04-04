"""Module for generating a job pitch for a job seeker."""

# pylint: disable=line-too-long

from utils.openai import OpenAIClient


def generate_pitch(job_seeker_name: str, job_description: str, company_name: str, extra_context: str = None) -> str:
    """
    Generates a compelling job pitch tailored to a specific job and company.

    Args:
        job_seeker_name (str): The name of the job seeker.
        job_description (str): The description of the job being applied for.
        company_name (str): The name of the company offering the job.
        extra_context (str, optional): Additional context to include in the pitch. Defaults to None.

    Returns:
        str: A pitch that highlights the job seeker's fit for the role and the company's culture/values.

    Raises:
        ValueError: If any required parameter is missing or empty.
        Exception: If the OpenAI API call fails (handled by OpenAIClient).

    Example:
        >>> pitch = generate_pitch(
        ...     job_seeker_name="Tomilola Oluwafemi",
        ...     job_description="Software Engineer: Develop scalable web applications using Python...",
        ...     company_name="TechCorp"
        ... )
        >>> print(pitch)
    """

    if not all([job_seeker_name, job_description, company_name]):
        raise ValueError(
            "Parameters (job_seeker_name, job_description, company_name) are required")

    prompt = (
        f"You are a career coach crafting a pitch for a job seeker named {job_seeker_name}. "
        f"The job seeker is applying for a position at {company_name} with the following job description: "
        f"'{job_description}'. "
        f"Write a concise, compelling pitch (150-200 words) that: "
        f"1) Highlights the job seeker's enthusiasm for the role and company, "
        f"2) Aligns their skills or experience with the job requirements, "
        f"3) Reflects an understanding of {company_name}'s culture and values (infer these from the job description if not explicit), "
        f"4) Uses a professional yet engaging tone. "
        f"and 5) ensure to sweeten the pitch with some extra context {extra_context} if provided."
        f"Focus on making the pitch persuasive and unique to this opportunity."
    )

    # Initialize client and send request
    client = OpenAIClient()
    messages = [{"role": "system", "content": prompt}]

    # Get response
    response = client.chat(messages)
    return response
